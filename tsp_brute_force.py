# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:15:49 2025

@author: sun
"""

import itertools

# Define the cities and distances
cities = ['A', 'B', 'C', 'D']
distances = {
    ('A', 'B'): 10,
    ('A', 'C'): 15,
    ('A', 'D'): 20,
    ('B', 'C'): 40,
    ('B', 'D'): 25,
    ('C', 'D'): 30
}

# Function to calculate the total cost of a route
def calculate_cost(route):
    total_cost = 0
    n = len(route)
    for i in range(n):
        current_city = route[i]
        next_city = route[(i + 1) % n]  # Wrap around to the start of the route
        # Look up the distance in both directions
        if (current_city, next_city) in distances:
            total_cost += distances[(current_city, next_city)]
        else:
            total_cost += distances[(next_city, current_city)]
    return total_cost

# Generate all permutations of the cities
all_permutations = itertools.permutations(cities)

# Initialize variables to track the minimum cost and corresponding route
min_cost = float('inf')
optimal_route = None

# Iterate over all permutations and calculate costs
for perm in all_permutations:
    cost = calculate_cost(perm)
    if cost < min_cost:
        min_cost = cost
        optimal_route = perm + ('A',)

# Print the optimal route and its cost
print(f"Optimal Route: {optimal_route}")
print(f"Total Cost: {min_cost}")