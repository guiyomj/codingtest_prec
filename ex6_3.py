# 퀵정렬: 피벗(기준 데이터)를 설정한 후 왼쪽에서는 피벗보다 큰, 오른쪽에서는 피벗보다 작은 데이터를 찾아서 위치 교환, O(nlogn)
arr=[5,7,9,0,3,1,6,2,4,8]
def quick(arr,start,end):
    if start>=end: return
    pivot = arr[start]
    left=start+1
    right=end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left+=1
        while start+1 <= right and arr[right] >= arr[pivot]:
            right-=1
        if left > right:
            arr[right],arr[pivot]=arr[pivot],arr[right]
        else:
            arr[left],arr[right]=arr[right],arr[left]

    quick(arr,start,right)
    quick(arr,right+1,end)


quick(arr,0,len(arr)-1)
print(arr)