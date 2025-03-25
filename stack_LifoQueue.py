# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:31:38 2025

@author: sun
"""

'''
queue 클래스의 LifoQueue 메소드 사용
스택 객체 생성후 데이터 삽입 put()
데이터 삭제 get()메소드 이용함
'''
import queue

# 스택 객체 생성하기
data_stack = queue.LifoQueue()

# 데이터 삽입
data_stack.put(10)
data_stack.put(20)
print("삽입된 데이터 크기 : ", data_stack.qsize())

# 데이터 삭제
print("데이터 삭제 : ", data_stack.get())