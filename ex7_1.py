'''
순차탐색: 앞에서부터 차례로 확인, O(n)
이진탐색: 시작값, 중간값, 끝값 활용, O(logn) => 데이터가 정렬되어 있어야 사용 가능
이진탐색트리: 왼쪽 자식노드 < 부모노드 < 오른쪽 자식노드
'''

arr = [1,3,5,7,9,11,13,15,17,19]
def binary(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target: return mid
        elif arr[mid] > target:
            end = mid-1
        else: start = mid+1

print(binary(arr,7,0,len(arr)-1))