# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:15:34 2025

@author: sun
"""

def unique_elements_1(A) :	    # 리스트 A입력
    n = len(A)		            # 입력의 크기 = 리스트의 크기
    for i in range(n-1) :	    # i : 0, 1, ... n-2
        for j in range(i+1,n) :	# j : i+1, i+2, ... n-1
            if A[i] == A[j] :	# 기본 연산
                return False	# 같은 항목이 있으면 True 반환
    return True		            # 같은 항목이 없으면 False 반환

# 2단계 알고리즘
def unique_elements_2(A) :
    A.sort()
    n = len(A)	            # 입력의 크기 = 리스트의 크기
    for i in range(n -1) :	    # i : 0, 1, ... n-2
        if A[i] == A[i + 1] :	# 기본 연산
                return False	# 같은 항목이 있으면 True 반환
    return True		            # 같은 항목이 없으면 False 반환

A = [32, 14, 5, 17, 23, 9, 11, 14, 26, 29]
B = [13, 6, 8, 7, 12, 25]
print(A, unique_elements_1(A))
print(B, unique_elements_1(B))

print(A, unique_elements_2(A))
print(B, unique_elements_2(B))