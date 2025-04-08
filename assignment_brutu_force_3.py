# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:55:17 2025

@author: sun
"""

import heapq

N = 4

# Function to calculate the least promising cost
def calculate_cost(cost_matrix, x, y, assigned):
    cost = 0
    available = [True] * N
    
    for i in range(x + 1, N):
        min_cost = float('inf')
        min_index = -1
        for j in range(N):
            if not assigned[j] and available[j] and cost_matrix[i][j] < min_cost:
                min_index = j
                min_cost = cost_matrix[i][j]
        
        cost += min_cost
        available[min_index] = False
    
    return cost

# Print the assignments
def print_assignments(node):
    if node['parent'] is None:
        return
    print_assignments(node['parent'])
    print(f"Assign Worker {chr(node['worker_id'] + ord('A'))} to Job {node['job_id']}")

# Finds minimum cost using Branch and Bound
def find_min_cost(cost_matrix):
    pq = []
    
    # Initialize with dummy node
    assigned = [False] * N
    root = {
        'worker_id': -1,
        'job_id': -1,
        'assigned': assigned[:],
        'parent': None,
        'path_cost': 0,
        'cost': 0
    }
    
    heapq.heappush(pq, (root['cost'], root))
    
    while pq:
        # Get the node with the least estimated cost
        _, min_node = heapq.heappop(pq)
        
        # Next worker to assign a job
        i = min_node['worker_id'] + 1
        
        if i == N:
            print("Optimal solution found:")
            print_assignments(min_node)
            return min_node['cost']
        
        for j in range(N):
            if not min_node['assigned'][j]:
                # Create a new tree node (using a dictionary)
                child_assigned = min_node['assigned'][:]
                child_assigned[j] = True
                
                child = {
                    'worker_id': i,
                    'job_id': j,
                    'assigned': child_assigned,
                    'parent': min_node,
                    'path_cost': min_node['path_cost'] + cost_matrix[i][j],
                    'cost': 0
                }
                
                child['cost'] = child['path_cost'] + calculate_cost(cost_matrix, i, j, child_assigned)
                
                # Debugging: print the cost and state of the child node
                print(f"Child node for worker {i} and job {j} has cost {child['cost']}")
                
                heapq.heappush(pq, (child['cost'], child))
    
    return -1  # Return -1 if no solution is found

# Driver code
if __name__ == "__main__":
    cost_matrix = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]
    
    optimal_cost = find_min_cost(cost_matrix)
    
    if optimal_cost != -1:
        print("\nOptimal Cost is", optimal_cost)
    else:
        print("No solution found")
