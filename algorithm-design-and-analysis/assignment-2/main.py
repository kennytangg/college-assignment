def prims_algorithm(graph, num_vertices):
    start = 0
    total_cost = 0
    seen_vertices = set()
    seen_vertices.add(start)
    mst_edges = []

    while len(seen_vertices) < num_vertices:
        minimum_weight = float("inf")
        best_from_vertex = None
        best_to_vertex = None

        for current_vertex in seen_vertices:
            for neighbor, weight in graph[current_vertex]:
                if neighbor not in seen_vertices:
                    if weight < minimum_weight:
                        minimum_weight = weight
                        best_from_vertex = current_vertex
                        best_to_vertex = neighbor

        if best_to_vertex is not None:
            seen_vertices.add(best_to_vertex)
            mst_edges.append((best_from_vertex, best_to_vertex, minimum_weight))

            total_cost += minimum_weight

            print(
                f"Added edge: {best_from_vertex} -> {best_to_vertex}, weight = {minimum_weight}"
            )

    return mst_edges, total_cost


def kruskals_algorithm(edges, num_vertices):
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    for edge in sorted_edges:
        print(f"  {edge[0]} - {edge[1]}: weight {edge[2]}")

    parent = []
    for i in range(num_vertices):
        parent.append(i)

    # Find which tree this vertex belong to
    def find_root(vertex):
        if parent[vertex] == vertex:
            return vertex
        else:
            parent[vertex] = find_root(parent[vertex])
            return parent[vertex]

    # Check if two vertices are in same set
    def are_connected(vertex1, vertex2):
        return find_root(vertex1) == find_root(vertex2)

    # Merge two sets
    def union_sets(vertex1, vertex2):
        root1 = find_root(vertex1)
        root2 = find_root(vertex2)

        # This connects the two trees
        parent[root2] = root1

    mst_edges = []
    total_cost = 0
    edges_added = 0

    for vertex1, vertex2, weight in sorted_edges:
        if not are_connected(vertex1, vertex2):
            mst_edges.append((vertex1, vertex2, weight))
            total_cost += weight
            edges_added += 1

            union_sets(vertex1, vertex2)

            print(f"Added edge: {vertex1} - {vertex2}, weight = {weight}")

            # Stop when we have enough edges
            if edges_added == num_vertices - 1:
                break
        else:
            print(
                f"Skipped edge: {vertex1} - {vertex2}, weight = {weight} (would create cycle)"
            )

    return mst_edges, total_cost
