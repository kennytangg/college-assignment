CC      = gcc
CFLAGS  = -Wall -Wextra -g -pthread
TARGETS = own_sem std_sem

.PHONY: all clean run time

all: $(TARGETS)

own_sem: own_sem.c
	$(CC) $(CFLAGS) -o $@ $<

std_sem: std_sem.c
	$(CC) $(CFLAGS) -o $@ $<

# Run both versions normally (no timing)
run: all
	@echo ""; echo ">>> Running OWN SEMAPHORE version..."; echo ""
	@> input.txt
	./own_sem
	@echo ""; echo ">>> Running STANDARD SEMAPHORE version..."; echo ""
	@> input.txt
	./std_sem

# Run both with `time` to measure execution time
time: all
	@echo ""; echo ">>> Timing OWN SEMAPHORE version..."; echo ""
	@> input.txt
	time ./own_sem
	@echo ""; echo ">>> Timing STANDARD SEMAPHORE version..."; echo ""
	@> input.txt
	time ./std_sem

clean:
	rm -f $(TARGETS) output_own.txt output_std.txt
	@> input.txt
