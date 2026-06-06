from utils import calculate_head_movements


def fcfs(start, requests):
    return calculate_head_movements(start, list(requests))


def scan(start, requests):
    # Initial direction: towards higher cylinder numbers (innermost)
    right = sorted(r for r in requests if r >= start)
    left = sorted((r for r in requests if r < start), reverse=True)
    sequence = right + left
    return calculate_head_movements(start, sequence)
