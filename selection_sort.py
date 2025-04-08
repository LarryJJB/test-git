# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 23:05:04 2025

@author: sun
"""
def printStep(arr, val) :
    print(" Step %2d = " % val, end='')
    print(arr)

def selection_sort(arr):
    n = len(arr) #데이터개수 확인
    for i in range( n - 1):
        least = i
        for j in range(i + 1, n):
            if arr[j] < arr[least]:
                least = j
        arr[i], arr[least] = arr[least], arr[i] #인덱스를 서로 교환. 
        printStep(arr, i+1)
        
#  데이터 입력
data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

# 원 데이터 출력
print("Original : ", data)

# 선택 정렬
selection_sort(data)

print("Selection : ", data)
