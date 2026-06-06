# Assignment 2 - Disk Scheduling

Name: Kenny Tang
Student ID: 2802517733

Implements FCFS and SCAN disk scheduling algorithms for a 5,000-cylinder disk (0–4999).

## Usage

```bash
python main.py -file input.txt -head 300
```

## Output

- **Task 1:** Head movements for FCFS and SCAN on the original request order.
- **Task 2:** Head movements after rearranging at most 500 of the 1,000 requests to minimize movements.

## Files

- `main.py` — entry point
- `scheduling.py` — FCFS and SCAN algorithms
- `optimizer.py` — Task 2 request rearrangement
- `utils.py` — file reading and movement calculation
