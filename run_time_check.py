# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:42:22 2025

@author: sun
"""

# 실행 시간 검사
import time

def summation(first, end) :
    sumVal = 0
    for i in range(first, end + 1) : 
        sumVal = sumVal + i
    
    return sumVal

# 입력
first = 1
end = 1000000

# 시작 시간
start_time = time.time()
# 실행 시간 측정 알고리즘
summation(first, end)

# 종료 시간 측정
end_time = time.time()

# 실행 시간
run_time = end_time - start_time

print("실행 시간 : ", run_time)
