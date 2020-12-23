# 삽입정렬: 두 번째 원소부터 시작하여 맨 앞 원소들과 크기 비교, O(n^2)
arr=[7,5,9,0,3,1,6,2,4,8]
start=1
for i in range(1,len(arr)):
    for j in range(0,i):
        if arr[j]>arr[i]: arr[j],arr[i]=arr[i],arr[j]
print(arr)