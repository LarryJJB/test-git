# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:03:14 2025
orginal : https://gist.github.com/YJDave/c9ad61598bbe6d059ef0396b77bbd612
@author: sun
"""

import itertools

def brute_force(weights, values, capacity):
    max_val = 0
    n = len(weights)
    all_combinations = [[0,1] for i in range(n)]

    for c in itertools.product(*all_combinations):
        val = 0
        w = 0
        for i in range(len(c)):
            if w > capacity:
                break

            val += c[i] * values[i]
            w += c[i] * weights[i]

        if w <= capacity and val > max_val:
            max_val = val

    return max_val


examples = [
        [[10, 20, 30], [60, 100, 120],  50],
        [[1, 2, 3], [10, 15, 40],  6],
        [[10, 20, 30], [60, 100, 120],  50],
        [[1, 2], [10, 15],  6],
        [[1, 2, 3, 4, 5], [10, 15, 10,20,30],  6]    
    ]


print(brute_force(*examples[0]))

