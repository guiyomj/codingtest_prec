# sys.stdin.readline()을 사용하면 빠르게 입력을 받을 수 있음
import sys

n=int(input())
nlst=list(map(int,sys.stdin.readline().split()))
m=int(input())
mlst=list(map(int,sys.stdin.readline().split()))

''' 일반적인 방법
for i in mlst:
    if i in nlst: print("yes",end=" ")
    else: print("no",end=" ")
'''

''' 계수정렬
nlst.sort()
chk=[0]*(nlst[-1]+1)
for i in nlst:
    chk[i]+=1
for i in mlst:
    if chk[i] != 0: print("yes",end=" ")
    else: print("no", end=" ")
'''

# 이진탐색
nlst.sort()
def binary(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target: return True
        elif arr[mid] > target:
            end = mid-1
        else: start = mid+1
    return False

for i in mlst:
    if binary(nlst,i,0,len(nlst)-1) == True:
        print("yes",end=" ")
    else: print("no",end=" ")