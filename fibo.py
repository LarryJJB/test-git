n = 7

#스택을 사용용
def fibo(n):
    #탈출조건 : 초기값
    if n == 1 or n ==2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

value = fibo(n)

print(value)

#숙제 : 어떤어떤이유를 가지고, 반복문을 사용할 것 같다. ~~이유가 되니까 리커시브를 쓸 것 같다. 시간체크해보니 ~~랬다. 또는 다른 이유도. 팩토리얼에 대해서.