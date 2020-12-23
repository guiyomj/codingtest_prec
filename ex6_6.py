n=int(input())
dic=list()
for i in range(n):
    t=input().split()
    dic.append([t[0],int(t[1])])
dic=sorted(dic,key=lambda dic:dic[1]) # lambda 변수:함수내용
for i in dic:
    print(i[0], end=" ")