# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:51:39 2025

@author: sun
"""

'''
queue 클래스의 PriorityQueue 메소드 사용
우선순위 큐 객체 생성후 데이터 삽입 put()
데이터 삭제 get()메소드 이용함
'''
import queue

# 우선순위 큐 객체 생성하기
data_priortity_queue = queue.PriorityQueue()

# 데이터 삽입 : 튜플로 (우선순위, value)
data_priortity_queue.put((10, 5))
data_priortity_queue.put((1, 10))
data_priortity_queue.put((5, 100))
print("삽입된 데이터 크기 : ", data_priortity_queue.qsize())

# 데이터 삭제
print("데이터 삭제 : ", data_priortity_queue.get())