# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:53:48 2025

@author: sun
"""

def gcd_1(m,n):
    while n != 0:
       t = m % n
       (m, n) = (n, t)
    return abs(m)

def gcd_2(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0 :
        return n
    else:
        return gcd_2(n, m % n)
       
def gcd_3(m,n):
    if n == 0:
        return m
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd_3(m, n)
    else:
        return n
    
# 60과 28 최대 공약수 구하기
max_div = gcd_1(60, 28)

# 최대 공약수 출력하기
print("gcd_1 최대 공약수 : ", max_div)
print("gcd_2 최대 공약수 : ", gcd_2(60, 28))
print("gcd_3 최대 공약수 : ", gcd_2(60, 28))