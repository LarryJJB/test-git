# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:26:58 2025

@author: sun
"""

# 최대값 찾기 함수 
def find_max( x ): 
    max = x[0]
    for i in range(len(x)) :
        if x[i] > max :
            max = x[i]
    return max

# 배열 데이터 : 리스트 초기화 이용하기
data = [ 20, 34, 12, 93, 84, 39, 64, 55, 24 ]

# 최대값 찾기
maxVal = find_max(data)

# 최대값 출력하기
print("배열 데이터 : ", data )
print("최댓값 = ", maxVal )