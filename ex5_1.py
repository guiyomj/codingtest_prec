# 반복적으로 구현한 팩토리얼
def fac1(n):
    ans = 1
    for i in range(n):
        ans*=(i+1)
    return ans

def fac2(n):
    if n==1:
        return 1
    elif n>1:
        return n*fac2(n-1)

if __name__=='__main__':
    print(fac1(5),fac2(5))