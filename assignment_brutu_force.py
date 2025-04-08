# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:19:05 2025

@author: sun
"""

import numpy as np


def all_pairs(lst):
    if len(lst) < 2:
        yield lst
        return
    a = lst[0]
    for i in range(1, len(lst)):
        pair = (a, lst[i])
        for rest in all_pairs(lst[1:i] + lst[i + 1:]):
            yield [pair] + rest


def brute_force_even(cost_matrix, idx_list=None):

    best_score = None
    best_assignment = []
    if idx_list is None:
        idx_list = [idx for idx in range(cost_matrix.shape[0])]

    for assignment in all_pairs(idx_list):

        # Build score
        assign_mat = np.zeros(cost_matrix.shape)
        for pair in assignment:
            if not isinstance(pair, tuple):
                continue
            assign_mat[pair[0], pair[1]] = 1
            assign_mat[pair[1], pair[0]] = 1
        score = np.sum(np.multiply(assign_mat, cost_matrix))

        # Check if we got a better score
        if best_score is None or score < best_score:
            best_assignment = assignment
            best_score = score

    return best_assignment, best_score

def bf_assign(cost_matrix):

    best_score = None
    best_assignment = []

    if cost_matrix.shape[0] % 2 == 1:
        odd_cnt = 0
        best_score = None
        best_assignment = []
        for removed in range(cost_matrix.shape[0]):
            idx_list = [idx for idx in range(cost_matrix.shape[0]) if idx != removed]
            odd_cnt = odd_cnt + 1
            tmp_assign, tmp_score = brute_force_even(cost_matrix, idx_list)
            if best_score is None or tmp_score < best_score:
                best_assignment = tmp_assign
                best_score = tmp_score
        return best_assignment, best_score
    else:
        return brute_force_even(cost_matrix)
    
# Generate random cost matrix
nb_agents = 5
cost_matrix = np.random.rand(nb_agents, nb_agents)
for row_idx in range(cost_matrix.shape[0]):
    for col_idx in range(row_idx, cost_matrix.shape[1]):
        if row_idx == col_idx:
            cost_matrix[row_idx, col_idx] = 0
        else:
            cost_matrix[col_idx, row_idx] = cost_matrix[row_idx, col_idx]

# 할당문제 해결하기            
bf_assignment, bf_score =bf_assign(cost_matrix)

print(bf_assignment)

#print('Brute force score: %s (computed in %s)' % (np.sum([cost_matrix[couple] for couple in bf_assignment]), datetime.now() - start_time)) 