# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:33:01 2025

@author: sun
"""

def getMyDivisor(n):
    divisorsList = []

    # 약수 구하기
    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)

    return divisorsList

# gcd구하기
def gcd(a, b) :
    a_div = getMyDivisor(a)
    
    # 큰 약수에서 작은 약수로 정렬하기
    a_div.sort(reverse=True)
    
    # 공통약수 구하기
    for element in a_div:
        if (b % element) == 0 :
            return element
  
# 60과 28 최대 공약수 구하기
max_div = gcd(60, 28)

# 최대 공약수 출력하기
print("최대 공약수 : ", max_div)
