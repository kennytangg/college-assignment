def read_requests(filepath):
    requests = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            for part in line.replace(',', ' ').split():
                requests.append(int(part.strip()))
    return requests


def calculate_head_movements(start, sequence):
    total = 0
    current = start
    for pos in sequence:
        total += abs(pos - current)
        current = pos
    return total
