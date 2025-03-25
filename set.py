# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:45:44 2025

@author: sun
"""
s_1 = {1, 2, 3}
#s_1 = set([1,2,3])
s_2 = {2, 3, 4,5}

# 합집합
s_3 = s_1.union(s_2)
#교집합
s_4 = s_1.intersection(s_2)

# 결과 출력
print("합집합 : ", s_3)
print("교집합 : ", s_4)