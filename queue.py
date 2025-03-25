# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:41:24 2025

@author: sun
"""

'''
queue 클래스의 Queue 메소드 사용
큐 객체 생성후 데이터 삽입 put()
데이터 삭제 get()메소드 이용함
'''
import queue

# 스택 객체 생성하기
data_queue = queue.Queue()

# 데이터 삽입
print("데이터 삽입 전 큐 사이즈 : ", data_queue.qsize())
data_queue.put(10)
data_queue.put(20)
print("데이터 삽입 후 큐 사이즈 : ", data_queue.qsize())

# 데이터 삭제
print("데이터 삭제 : ", data_queue.get())
print("데이터 삭제 후 큐 사이즈 : ", data_queue.qsize())
