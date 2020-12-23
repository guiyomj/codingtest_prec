'''
loc=input()
loc=[ord(loc[0])-97,int(loc[1])]
t=(loc[0]>3 and 7-loc[0] or loc[0])+(loc[1]>3 and 7-loc[1] or loc[1])
if t <= 1:
    print(2)
elif t <= 2 or loc[0] == 0 or loc[1] == 0:
    print(4)
elif loc[0] == 1 or loc[1] == 1:
    print(6)
else:
    print(8)
'''
loc=input()
loc=[ord(loc[0])-ord('a')+1,int(loc[1])]
move=[
    [-2,-1], [-1,-2], [2, 1], [1, 2],
    [-2, 1], [-1, 2], [2, -1], [1, -2]
]
ans=0
for i in move:
    if 8 >= loc[0]+i[0] >= 1 and 8 >= loc[1]+i[1] >= 1:
        ans+=1
print(ans)