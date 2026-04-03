#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define NUM_READERS 2
#define NUM_WRITERS 2
#define NUM_OPS 5
#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "output_own.txt"
#define MAX_LINE 512

/* Own semaphore: a counter protected by a mutex + condition variable */
typedef struct {
  int value;
  pthread_mutex_t lock;
  pthread_cond_t cond;
} own_sem_t;

void own_sem_init(own_sem_t *s, int val) {
  s->value = val;
  pthread_mutex_init(&s->lock, NULL);
  pthread_cond_init(&s->cond, NULL);
}

void own_sem_wait(own_sem_t *s) {
  pthread_mutex_lock(&s->lock);
  while (s->value == 0)
    pthread_cond_wait(&s->cond, &s->lock);
  s->value--;
  pthread_mutex_unlock(&s->lock);
}

void own_sem_signal(own_sem_t *s) {
  pthread_mutex_lock(&s->lock);
  s->value++;
  pthread_cond_signal(&s->cond);
  pthread_mutex_unlock(&s->lock);
}

void own_sem_destroy(own_sem_t *s) {
  pthread_mutex_destroy(&s->lock);
  pthread_cond_destroy(&s->cond);
}

static own_sem_t rw_sem;
static own_sem_t mutex_sem;
static int reader_count = 0;
static FILE *out_fp = NULL;

static void timestamp(char *buf, size_t len) {
  struct timespec ts;
  clock_gettime(CLOCK_REALTIME, &ts);
  struct tm *t = localtime(&ts.tv_sec);
  char base[32];
  strftime(base, sizeof(base), "%H:%M:%S", t);
  snprintf(buf, len, "%s.%03ld", base, ts.tv_nsec / 1000000);
}

static void read_last_line(char *buf, size_t len) {
  FILE *fp = fopen(INPUT_FILE, "r");
  if (!fp) {
    snprintf(buf, len, "(cannot open file)");
    return;
  }

  fseek(fp, 0, SEEK_END);
  long size = ftell(fp);
  if (size == 0) {
    snprintf(buf, len, "(file is empty)");
    fclose(fp);
    return;
  }

  long pos = size - 1;
  char c;

  /* skip trailing newlines */
  fseek(fp, pos, SEEK_SET);
  fread(&c, 1, 1, fp);
  while (pos > 0 && (c == '\n' || c == '\r')) {
    fseek(fp, --pos, SEEK_SET);
    fread(&c, 1, 1, fp);
  }

  /* walk back to start of last line */
  while (pos > 0) {
    fseek(fp, pos - 1, SEEK_SET);
    fread(&c, 1, 1, fp);
    if (c == '\n')
      break;
    pos--;
  }

  fseek(fp, pos, SEEK_SET);
  if (!fgets(buf, (int)len, fp))
    snprintf(buf, len, "(read error)");
  buf[strcspn(buf, "\r\n")] = '\0';
  fclose(fp);
}

void *reader_thread(void *arg) {
  int id = *(int *)arg;
  char line[MAX_LINE], ts[32];

  for (int i = 1; i <= NUM_OPS; i++) {
    own_sem_wait(&mutex_sem);
    reader_count++;
    if (reader_count == 1)
      own_sem_wait(&rw_sem);
    own_sem_signal(&mutex_sem);

    read_last_line(line, sizeof(line));
    timestamp(ts, sizeof(ts));
    printf("[OWN] Reader-%d | read #%d | %s | \"%s\"\n", id, i, ts, line);
    fprintf(out_fp, "[OWN] Reader-%d | read #%d | %s | \"%s\"\n", id, i, ts,
            line);
    fflush(out_fp);

    own_sem_wait(&mutex_sem);
    reader_count--;
    if (reader_count == 0)
      own_sem_signal(&rw_sem);
    own_sem_signal(&mutex_sem);

    usleep(100000);
  }
  return NULL;
}

void *writer_thread(void *arg) {
  int id = *(int *)arg;
  char ts[32];

  for (int i = 1; i <= NUM_OPS; i++) {
    own_sem_wait(&rw_sem);

    timestamp(ts, sizeof(ts));
    FILE *fp = fopen(INPUT_FILE, "a");
    if (fp) {
      fprintf(fp, "Writer-%d | write #%d | %s\n", id, i, ts);
      fclose(fp);
    }
    printf("[OWN] Writer-%d | write #%d | %s\n", id, i, ts);

    own_sem_signal(&rw_sem);
    usleep(150000);
  }
  return NULL;
}

int main(void) {
  own_sem_init(&rw_sem, 1);
  own_sem_init(&mutex_sem, 1);

  out_fp = fopen(OUTPUT_FILE, "w");
  if (!out_fp) {
    perror("fopen output");
    return EXIT_FAILURE;
  }

  FILE *inp = fopen(INPUT_FILE, "w");
  if (!inp) {
    perror("fopen input");
    return EXIT_FAILURE;
  }
  fclose(inp);

  pthread_t readers[NUM_READERS], writers[NUM_WRITERS];
  int r_ids[NUM_READERS], w_ids[NUM_WRITERS];

  printf("=== OWN SEMAPHORE ===\n");
  fprintf(out_fp, "=== OWN SEMAPHORE ===\n");

  for (int i = 0; i < NUM_WRITERS; i++) {
    w_ids[i] = i + 1;
    pthread_create(&writers[i], NULL, writer_thread, &w_ids[i]);
  }
  usleep(50000);
  for (int i = 0; i < NUM_READERS; i++) {
    r_ids[i] = i + 1;
    pthread_create(&readers[i], NULL, reader_thread, &r_ids[i]);
  }

  for (int i = 0; i < NUM_WRITERS; i++)
    pthread_join(writers[i], NULL);
  for (int i = 0; i < NUM_READERS; i++)
    pthread_join(readers[i], NULL);

  printf("=== DONE — output: %s ===\n", OUTPUT_FILE);
  fprintf(out_fp, "=== DONE ===\n");

  fclose(out_fp);
  own_sem_destroy(&rw_sem);
  own_sem_destroy(&mutex_sem);
  return EXIT_SUCCESS;
}
