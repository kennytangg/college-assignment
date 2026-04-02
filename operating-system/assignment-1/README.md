# Assignment 1: Multi-threaded Producer-Consumer

This assignment 1 is also the forum for session 6. A thread-safe Producer-Consumer implementation in C using a bounded stack buffer and POSIX condition variables (`pthread_cond_t`). 

## How it Works
- **1 Producer** generates 10,000 random numbers, pushes them to a stack buffer, and logs them to `all.txt`.
- **2 Consumers** (Even and Odd) read from the stack. They only pop and write numbers matching their parity to `even.txt` or `odd.txt`.

## Compile & Run

```bash
gcc -O2 -o main main.c -lpthread
time ./main
```

## Sample Output

```bash
$ time ./main
Done. produced=10000  consumed=10000
./main  0.02s user 0.04s system 134% cpu 0.045 total
```
