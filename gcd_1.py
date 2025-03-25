# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:55:13 2025

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
    b_div = getMyDivisor(b)
    
    # 공통약수 구하기
    div = []
    for i in range(len(a_div)):
        for j in range(len(b_div)):
            if a_div[i] == b_div[j]:
                div.append(a_div[i])
                
    # 최대 공약수 구하기
    max_div = max(div)
    
    return max_div

# 60과 28 최대 공약수 구하기
max_div = gcd(60, 28)

# 최대 공약수 출력하기
print("최대 공약수 : ", max_div)
