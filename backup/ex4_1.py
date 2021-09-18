n=int(input())
locx=1
locy=1
lst=input().split()
for i in lst:
    if i == 'U':
        locy = locy>1 and locy-1 or locy
    elif i == 'D':
        locy = locy<n and locy+1 or locy
    elif i == 'L':
        locx = locx>1 and locx-1 or locx
    else:
        locx = locx<5 and locx+1 or locx
print(locy,locx)