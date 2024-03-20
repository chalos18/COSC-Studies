def iterate_vertices(adj_list):
    vertices = set()  # Using a set to avoid duplicates

    # Iterate through each sublist in the adjacency list
    for sublist in adj_list:
        # Iterate through each vertex in the sublist
        for vertex, _ in sublist:
            # Add the vertex to the set
            vertices.add(vertex)

    return vertices


# Example adjacency list representation of a graph
adj_list = [[(1, 5), (2, 3)], [(0, 1)], [(3, 2)], [(2, 7)]]

# Call the function and print the result
vertices = iterate_vertices(adj_list)
print("Vertices:", vertices)
