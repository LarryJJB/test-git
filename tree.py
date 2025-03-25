# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:37:45 2025

@author: sun
"""

# 트리 배열로 만들기
tree = ["A", "B", "C", "D", "E", "F", None, "G"]

# 트리 그려보기
n = len(tree)
for i in range(n):
    if tree[i] is not None:  # 현재 노드가 None이 아닐 때
        print(f"Parent: {tree[i]}", end=", ")
        left = 2 * i + 1  # 왼쪽 자식 노드
        right = 2 * i + 2  # 오른쪽 자식 노드

        if left < n and tree[left] is not None:  # 왼쪽 자식이 배열 범위 안에 있을 때
            print(f"Left: {tree[left]}", end=", ")
        if right < n and tree[right] is not None:  # 오른쪽 자식이 배열 범위 안에 있을 때
            print(f"Right: {tree[right]}", end=" ")
        print()