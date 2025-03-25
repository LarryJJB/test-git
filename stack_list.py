# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:22:44 2025

@author: sun
"""

# 데이터 입력
data = [1, 2, 3, 4, 5]
#data = [x for x in range(1, 6)]

# 데이터 삽입
data.append(10)
data.append(11)
print('삽입된 데이터 : ', data)

# 데이터 삭제
data.pop()
print('삭제된 데이터 : ', data)
data.pop(-1)
print('삭제된 데이터 : ', data)