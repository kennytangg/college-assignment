# MST Algorithms - Optimized for Large Graphs
# Prim's: O(E log V) with binary heap
# Kruskal's: O(E log E) with Union-Find (rank + path compression)

import heapq
import time

def parse_graph(filename):
    edges = []
    print(f"Loading {filename}...", end=" ")
    start = time.time()

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if parts[0] == "a":
                edges.append((int(parts[1]), int(parts[2]), int(parts[3])))

    max_vertex = max(max(u, v) for u, v, _ in edges)
    num_vertices = max_vertex + 1

    print(f"Done ({time.time() - start:.3f}s)")
    print(f"Graph: {num_vertices} vertices, {len(edges)} edges\n")

    return edges, num_vertices


def build_adjacency(edges, n):
    adj = {i: [] for i in range(n)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj


# Prim's algorithm with binary heap O(E log V)
def prims_optimized(adj, n):
    in_mst = [False] * n
    heap = [(0, 0)]
    total = 0
    edges_count = 0

    while heap and edges_count < n:
        w, u = heapq.heappop(heap)

        if in_mst[u]:
            continue

        in_mst[u] = True
        total += w
        edges_count += 1

        for v, edge_weight in adj[u]:
            if not in_mst[v]:
                heapq.heappush(heap, (edge_weight, v))

    return total


# Kruskal's algorithm with Union-Find O(E log E)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


def kruskals_optimized(edges, n):
    sorted_edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(n)
    total = 0
    edges_added = 0

    for u, v, w in sorted_edges:
        if uf.union(u, v):
            total += w
            edges_added += 1
            if edges_added == n - 1:
                break

    return total


# Benchmark = run 10 times
def benchmark(func, *args, runs=10):
    times = []
    results = []

    for i in range(runs):
        start = time.time()
        result = func(*args)
        elapsed = time.time() - start
        times.append(elapsed)
        results.append(result)

    return results, times


def main():
    filename = "data/standard.text"

    print("=" * 60)
    print("MST ALGORITHMS - BENCHMARK")
    print("=" * 60)
    print()

    # Load graph once
    edges, n = parse_graph(filename)
    adj = build_adjacency(edges, n)

    print("=" * 60)
    print("Running each algorithm 10 times")
    print("(Computation time only, excluding file loading)")
    print("=" * 60)
    print()

    # Prim's
    print("PRIM'S ALGORITHM")
    print("-" * 60)
    prim_results, prim_times = benchmark(prims_optimized, adj, n, runs=10)

    print(f"Total Distance: {prim_results[0]}")
    print(f"Average compute time: {sum(prim_times) / len(prim_times):.6f}s")
    print(f"Min compute time: {min(prim_times):.6f}s")
    print(f"Max compute time: {max(prim_times):.6f}s")
    print()

    # Kruskal's
    print("KRUSKAL'S ALGORITHM")
    print("-" * 60)
    kruskal_results, kruskal_times = benchmark(kruskals_optimized, edges, n, runs=10)

    print(f"Total Distance: {kruskal_results[0]}")
    print(f"Average compute time: {sum(kruskal_times) / len(kruskal_times):.6f}s")
    print(f"Min compute time: {min(kruskal_times):.6f}s")
    print(f"Max compute time: {max(kruskal_times):.6f}s")
    print()

    # Verification
    print("=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    print(f"Both algorithms agree: {prim_results[0] == kruskal_results[0]}")
    print(f"Total distance: {prim_results[0]}")
    print(f"All runs consistent: {len(set(prim_results)) == 1 and len(set(kruskal_results)) == 1}")
    print()

    # Performance comparison
    avg_prim = sum(prim_times) / len(prim_times)
    avg_kruskal = sum(kruskal_times) / len(kruskal_times)

    print("PERFORMANCE COMPARISON")
    print("-" * 60)
    print(f"Prim's avg:    {avg_prim:.6f}s")
    print(f"Kruskal's avg: {avg_kruskal:.6f}s")

    if avg_prim < avg_kruskal:
        print(f"Prim's is {avg_kruskal / avg_prim:.2f}x faster")
    else:
        print(f"Kruskal's is {avg_prim / avg_kruskal:.2f}x faster")
    print()


if __name__ == "__main__":
    main()