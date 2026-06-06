def optimize_requests(requests):
    """Rearrange at most half (500 of 1000) requests to minimize FCFS head movements.

    Strategy: sort the first 500 positions by value. This always stays within
    the rearrangement limit since only positions 0-499 can change, and it
    converts the first half of the traversal into a sorted (low-movement) sequence.
    """
    n = len(requests)
    limit = n // 2
    result = list(requests)
    result[:limit] = sorted(requests[:limit])
    return result
