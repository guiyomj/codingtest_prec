'''
# 다이나믹 프로그래밍: 메모리 공간을 효율적으로 이용하여 계산 -> 피보나치 수열 등에 효율적(시간복잡도 O(n))
조건
1. 큰 문제를 작은 문제로 나눌 수 있음(재귀)
2. 작은 문제에서 구한 정답 == 큰 문제에서 구한 정답

# 메모이제이션: DP의 한 종류, 결과를 메모리 공간에 저장해 두고 그 결과를 가져오는 방법
# 1000번 이상 재귀호출시 에러 -> sys 라이브러리의 sys.setrecursionlimit(10000)으로 설정
'''

import sys
sys.setrecursionlimit(1000000)
num=10

# 일반 피보나치 1 2 3 5 8 ...
def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

# 메모이제이션 피보나치
lst = [0]*(num+1)
def fibo2(n):
    if n<=1:
        return 1
    else:
        if lst[n] != 0:
            return lst[n]
            print("멤~")
        else:
            lst[n] = fibo2(n-1)+fibo2(n-2)
            return lst[n]

# 바텀업 피보나치(탑다운보다 권장)
lst2 = [1,1]+[0]*(num-1)
def fibo3(n):
    for i in range(2,n+1):
        lst2[i]=lst2[i-1]+lst2[i-2]

fibo3(num)
print(lst2[num])