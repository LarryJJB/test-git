import time

def factorial(n):            # 재귀적 방법
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_iter(n):      # 반복적 방법
    result = 1
    for k in range(n, 0, -1):
        result *= k
    return result

n = 900  # 테스트할 숫자

# 재귀적 방법 시간 측정
start_time = time.time()
try:
    factorial(n)
except RecursionError:
    print("Recursion limit exceeded for factorial(n)")
end_time = time.time()
rec_time = end_time - start_time
print(f"재귀적 방법 실행 시간: {rec_time:.6f}초")

# 반복적 방법 시간 측정
start_time = time.time()
factorial_iter(n)
end_time = time.time()
iter_time = end_time - start_time
print(f"반복적 방법 실행 시간: {iter_time:.6f}초")