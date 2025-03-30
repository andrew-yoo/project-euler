# Project Euler
# Longest Collatz Sequence
# Problem 14
# https://projecteuler.net/problem=14
#
# """
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# """

import numpy as np

def create_adjacency_matrix(rows, cols):
    total_nodes = rows * cols
    adjacency_matrix = np.zeros((total_nodes, total_nodes), dtype=int)

    def find_index(i, j):
        return i * cols + j

    for i in range(rows):
        for j in range(cols):
            current_node = find_index(i, j)
            if j + 1 < cols: # Add right unless on rightmost edge
                right_node = find_index(i, j + 1)
                adjacency_matrix[current_node, right_node] = 1
            
            if i + 1 < rows: # Add down unless on bottommost edge
                down_node = find_index(i + 1, j)
                adjacency_matrix[current_node, down_node] = 1
    return adjacency_matrix

def raise_power(adj_matrix, start_node, end_node, steps):
    total_routes = 0
    current_matrix = np.eye(len(adj_matrix), dtype=int)  # Identity matrix
    for step in range(steps):
        current_matrix = np.dot(current_matrix, adj_matrix)
        total_routes += current_matrix[start_node, end_node]
    return total_routes

# 20 x 20 grid = 21 x 21 nodes
rows = 21
cols = 21

adj_matrix = create_adjacency_matrix(rows, cols)

start_node = 0 # Starts at top left corner
end_node = rows * cols - 1 # Ends at bottom right corner

max_steps = (rows - 1) + (cols - 1) # Max steps = horizontal vertices + vertical vertices

# Raises matrix power - gets really slow for larger matrices
total_routes = raise_power(adj_matrix, start_node, end_node, max_steps)

print(total_routes)
