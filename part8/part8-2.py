'''
바텀업(상향식) 다이나믹 프로그래밍을 이용한 피보나치 수열 풀이
'''
d = [0] * 100
d[1] = 1
d[2] = 1
for i in range(3, 100):
    d[i] = d[i - 1] + d[i - 2]
def fibo(n):
    return d[n]
print(fibo(99))
