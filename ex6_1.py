# 선택정렬: 가장 작은 수를 찾아서 맨 앞으로 보내는 방식, O(n)
arr=[7,5,9,0,3,1,6,2,4,8]
start=0
while start != len(arr):
    m=min(arr[start:])
    m_idx=arr.index(m)
    arr[start],arr[m_idx]=m,arr[start]
    start+=1
print(arr)