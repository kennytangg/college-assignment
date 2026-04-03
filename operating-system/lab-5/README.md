# Lab 5 — Process Synchronization: Readers-Writers

This lab 5 is an optional assignment for session 5. 

## Build & Run

```bash
make        # build both
make run    # run both
make time   # run both with time measurement
make clean
```

## Algorithm

Readers-preference Readers-Writers using two binary semaphores:
- `rw_sem` — writer/reader-group exclusion
- `mutex_sem` — protects `reader_count`

`own_sem.c` implements the semaphore as a counter + `pthread_mutex_t` + `pthread_cond_t`.  
`std_sem.c` uses POSIX `sem_t` (`sem_wait` / `sem_post`). The algorithm is identical.

---

## Q1 — Own vs Standard Semaphore

Both versions produce the same output and behavior. The difference is only at the primitive level: the own semaphore manually blocks threads via a condition variable while the counter is 0, whereas `sem_t` does this inside the kernel (futex-based on Linux). Under low contention like this lab, the difference is negligible.

## Q2 — Running Times

```
# own_sem
0.00user 0.00system 0:00.75elapsed 0%CPU

# std_sem
0.00user 0.00system 0:00.75elapsed 0%CPU
```

Both versions ran in 0.75s. `real` time is dominated by `usleep()` delays, not synchronization overhead. `user` and `sys` are effectively zero for both — the own semaphore's condition variable adds no measurable cost at this scale.

## Q3 — Problems Encountered

**Empty file on first read** — readers starting before any writer finishes would `fseek` on an empty file. Fixed by checking `ftell() == 0` and returning `"(file is empty)"`.

**Trailing newline on last-line seek** — `fseek(SEEK_END)` lands after the final `\n`, making a naive `fgets` return empty. Fixed by walking backwards past trailing newlines before scanning for the line start.

**Non-deterministic writer order** — writers interleave unpredictably across runs. This is expected scheduler behavior, not a bug.
