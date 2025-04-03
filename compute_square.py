# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 18:27:37 2025

@author: sun
"""
# 알고리즘 A
def compute_square_A(n) :	# 정수 n의 제곱 계산 함수. 알고리즘 A 사용
    return n*n		# 기본 연산: n*n

# 알고리즘 B
def compute_square_B(n) :	# 정수 n의 제곱 계산 함수. 알고리즘 B 사용
    sum = 0
    for i in range(n) :	# i : 0, 1, ... n-1
    	sum = sum + n		# 기본 연산
    return sum

# 알고리즘 ㅊ
def compute_square_C(n) :	# 정수 n의 제곱 계산 함수. 알고리즘 C 사용
    sum = 0
    for i in range(n) :	# i : 0, 1, ... n-1
    	for j in range(n) :	# j : 0, 1, ... n-1
    		sum = sum + 1	# 기본 연산
    return sum	

print("11 square (A) = ", compute_square_A(11))
print("11 square (B) = ", compute_square_B(11))
print("11 square (C) = ", compute_square_C(11))

