import time
import matplotlib.pyplot as plt

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

n_values = list(range(3, 1000, 1))  # 10부터 10000까지 10 간격
rec_times = []
iter_times = []

for n in n_values:
    # 재귀적 방법 시간 측정
    start_time_1 = time.time()
    try:
        factorial(n)
    except RecursionError:
        rec_times.append(None)
    else:
        rec_times.append(time.time() - start_time_1)
    

for n in n_values:
    # 반복적 방법 시간 측정
    start_time_2 = time.time()
    try:
        factorial_iter(n)
    except RecursionError:
        iter_times.append(None)
    else:
        iter_times.append(time.time() - start_time_2)

# 그래프 그리기
plt.figure(figsize=(10, 5))
plt.plot(n_values, iter_times, label='loop', linestyle='-')
plt.plot(n_values, rec_times, label='recursive', linestyle='-')
plt.xlabel('n')
plt.ylabel('time (second)')
plt.title('loop vs recursive')
plt.legend()
plt.grid()
plt.xlim(0, 1000)
plt.show()