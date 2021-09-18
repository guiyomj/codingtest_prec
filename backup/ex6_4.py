# 계수정렬: 빈 배열 선언 후 횟수를 카운팅, O(n+k)
arr=[5,7,9,0,3,1,6,2,4,8]
arrr=[0]*(max(arr)+1)
for i in arr:
    arrr[i]+=1
for idx,i in enumerate(arrr):
    print(idx, end=" ")