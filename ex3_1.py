def func(n):
    lst=[500,100,50,10]
    ans=0
    for i in lst:
        ans+=n//i
        n-=i*(n//i)
    print(ans)
if __name__ == '__main__':
    n=1260
    func(n)