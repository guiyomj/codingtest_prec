n,m=map(int,input().split())
lst=list()
for i in range(n):
    tmp=input()
    lst.append([])
    for j in range(len(tmp)):
        lst[i].append(tmp[j])
print(lst)