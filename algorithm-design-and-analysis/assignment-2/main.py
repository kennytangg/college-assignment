# MST Algorithms
# Prim's: O(E log V) with binary heap
# Kruskal's: O(E log E) with Union-Find

import heapq
import time
import statistics
import math


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
    start_vertex = edges[0][0]

    print(f"Done ({time.time() - start:.3f}s)")

    return edges, num_vertices, start_vertex


def build_adjacency(edges, n):
    adj = {i: [] for i in range(n)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj


def calculate_graph_properties(n, e):
    max_edges = (n * (n - 1)) / 2
    density = (e / max_edges) * 100 if max_edges > 0 else 0
    avg_degree = (2 * e) / n if n > 0 else 0

    return {
        "density": density,
        "avg_degree": avg_degree,
        "is_sparse": density < 10,
        "is_dense": density > 50,
    }


def prims_optimized(adj, n, start_vertex):
    in_mst = [False] * n
    heap = [(0, start_vertex)]  # Use start_vertex instead of 0
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


def benchmark_detailed(func, *args, runs=10):
    times = []
    results = []

    print(f"\n{'Run':<6} {'Time (s)':<15} {'Distance':<15}")
    print("-" * 40)

    for i in range(1, runs + 1):
        start = time.time()
        result = func(*args)
        elapsed = time.time() - start
        times.append(elapsed)
        results.append(result)

        print(f"{i:<6} {elapsed:<15.8f} {result:<15,}")

    return results, times


def main():
    filename = "data/USA-road-d.COL.text"
    graph_name = filename.split("/")[-1].replace(".text", "").replace(".txt", "")

    # Load graph once
    edges, n, start_vertex = parse_graph(filename)
    e = len(edges)
    adj = build_adjacency(edges, n)

    print(f"Starting Prim's from vertex: {start_vertex}\n")

    # Graph properties
    props = calculate_graph_properties(n, e)

    print("GRAPH PROPERTIES:")
    print("-" * 70)
    print(f"Graph Name:        {graph_name}")
    print(f"Nodes (V):         {n:,}")
    print(f"Arcs (E):          {e:,}")
    print(f"Density:           {props['density']:.4f}%")
    print(f"Avg Degree:        {props['avg_degree']:.2f}")
    print(f"Sparse/Dense:      {'Sparse' if props['is_sparse'] else 'Dense'}")
    print()

    # Theoretical complexity
    print("THEORETICAL COMPLEXITY:")
    print("-" * 70)
    prim_complexity = e * math.log2(n) if n > 0 else 0
    kruskal_complexity = e * math.log2(e) if e > 0 else 0
    print(f"Prim's O(E log V):    {prim_complexity:.2e} operations")
    print(f"Kruskal's O(E log E): {kruskal_complexity:.2e} operations")
    print()

    # Prim's Algorithm
    print("=" * 70)
    print("PRIM'S ALGORITHM - 10 RUNS")
    print("=" * 70)
    prim_results, prim_times = benchmark_detailed(
        prims_optimized, adj, n, start_vertex, runs=10
    )

    print("\nPRIM'S STATISTICS:")
    print("-" * 70)
    print(f"Total Distance:    {prim_results[0]:,}")
    print(f"Average Time:      {statistics.mean(prim_times):.8f}s")
    print(f"Median Time:       {statistics.median(prim_times):.8f}s")
    print(f"Std Deviation:     {statistics.stdev(prim_times):.8f}s")
    print(f"Variance:          {statistics.variance(prim_times):.10f}")
    print(f"Min Time:          {min(prim_times):.8f}s")
    print(f"Max Time:          {max(prim_times):.8f}s")

    # Kruskal's Algorithm
    print("\n" + "=" * 70)
    print("KRUSKAL'S ALGORITHM - 10 RUNS")
    print("=" * 70)
    kruskal_results, kruskal_times = benchmark_detailed(
        kruskals_optimized, edges, n, runs=10
    )

    print("\nKRUSKAL'S STATISTICS:")
    print("-" * 70)
    print(f"Total Distance:    {kruskal_results[0]:,}")
    print(f"Average Time:      {statistics.mean(kruskal_times):.8f}s")
    print(f"Median Time:       {statistics.median(kruskal_times):.8f}s")
    print(f"Std Deviation:     {statistics.stdev(kruskal_times):.8f}s")
    print(f"Variance:          {statistics.variance(kruskal_times):.10f}")
    print(f"Min Time:          {min(kruskal_times):.8f}s")
    print(f"Max Time:          {max(kruskal_times):.8f}s")

    # Comparison data
    avg_prim = statistics.mean(prim_times)
    avg_kruskal = statistics.mean(kruskal_times)

    print("\n" + "=" * 70)
    print("COMPARISON DATA")
    print("=" * 70)
    print(f"Prim's avg time:       {avg_prim:.8f}s")
    print(f"Kruskal's avg time:    {avg_kruskal:.8f}s")
    print(f"Absolute difference:   {abs(avg_prim - avg_kruskal):.8f}s")
    print(
        f"Percentage difference: {abs(avg_prim - avg_kruskal) / min(avg_prim, avg_kruskal) * 100:.2f}%"
    )
    print(f"Faster algorithm:      {'Prim' if avg_prim < avg_kruskal else 'Kruskal'}")
    print(
        f"Speed ratio:           {max(avg_prim, avg_kruskal) / min(avg_prim, avg_kruskal):.2f}x"
    )

    # Verification
    print("\n" + "=" * 70)
    print("VERIFICATION")
    print("=" * 70)
    print(f"Algorithms agree:          {prim_results[0] == kruskal_results[0]}")
    print(f"Prim runs consistent:      {len(set(prim_results)) == 1}")
    print(f"Kruskal runs consistent:   {len(set(kruskal_results)) == 1}")

    # Table format
    print("\n" + "=" * 70)
    print("TABLE FORMAT")
    print("=" * 70)
    print(f"\nGraph: {graph_name} | Nodes: {n:,} | Arcs: {e:,}\n")
    print(
        f"{'Run':<5} | {'Prim Time (s)':>15} | {'Prim Dist':>12} | {'Kruskal Time (s)':>17} | {'Kruskal Dist':>13}"
    )
    print("-" * 85)
    for i in range(10):
        print(
            f"{i + 1:<5} | {prim_times[i]:>15.8f} | {prim_results[i]:>12,} | {kruskal_times[i]:>17.8f} | {kruskal_results[i]:>13,}"
        )
    print()


if __name__ == "__main__":
    main()
