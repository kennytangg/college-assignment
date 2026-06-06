import argparse

from utils import read_requests
from scheduling import fcfs, scan
from optimizer import optimize_requests


def parse_args():
    parser = argparse.ArgumentParser(description='Disk Scheduling Simulator')
    parser.add_argument('-file', required=True, help='Path to cylinder request file')
    parser.add_argument('-head', required=True, type=int, help='Initial head position')
    return parser.parse_args()


def print_task_results(label, fcfs_total, scan_total):
    print(f'{label}:')
    print(f'  FCFS: {fcfs_total} head movements')
    print(f'  SCAN: {scan_total} head movements')


def main():
    args = parse_args()
    requests = read_requests(args.file)
    head = args.head

    print_task_results('Task 1 - Original Order', fcfs(head, requests), scan(head, requests))
    print()
    optimized = optimize_requests(requests)
    print_task_results('Task 2 - Optimized Order', fcfs(head, optimized), scan(head, optimized))


if __name__ == '__main__':
    main()
