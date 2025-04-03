# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:10:43 2025

@author: sun
"""

def hanoi_tower(fr, tmp, to, n) :		        # Hanoi Tower 순환 함수
    if (n == 1) :				                # 종료 조건
        print("원판 1: %s --> %s" % (fr, to))	# 가장 작은 원판을 옮김
    else :
        hanoi_tower( fr, to, tmp, n - 1)		    # n-1개를  to를 이용해 tmp로
        print("원판 %d: %s --> %s" % (n,fr,to))	# 하나의 원판을 옮김
        hanoi_tower( tmp, fr, to, n - 1)		    # n-1개를  fr을 이용해 to로

# 하노이 탑
hanoi_tower( 'A', 'B', 'C', 4)

