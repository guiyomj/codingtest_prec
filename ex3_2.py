if __name__ == '__main__':
    n,m,k=map(int,input().split())
    lst=list(map(int,input().split()))
    ans=0
    cnt=0
    lst.sort()
    num1=lst[-1]
    num2=lst[-2]

    ans=num1*(m-(m//(k+1)))+num2*(m//(k+1))
    print(ans)