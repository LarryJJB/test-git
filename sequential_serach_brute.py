# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:54:33 2025

@author: sun
"""
def sequential_search(data, key):	# data는 입력 리스트, key는 탐색 키
    for i in range(len(data)) :	# i : 0, 1, ... len(A)-1
        if data[i] == key :  	# 탐색 성공하면 (비교연산. 기본 연산임)
            return i 			# 인덱스 반환 
    return -1					# 탐색에 실패하면 -1 반환 

# 검색할 데이터
data = [ 5, 3, 8, 4, 2, 7]

# 데이터 검색 결과
print("4찾기: ", sequential_search(data, 4))
print("6찾기: ", sequential_search(data, 6))
