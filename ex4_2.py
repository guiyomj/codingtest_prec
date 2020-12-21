n=int(input())
h_s=0
ans=0
while n>=h_s:
    if h_s == 3 or h_s == 13 : ans+=(60*60)
    else: ans+=(45*15)+(15*60)
    h_s+=1
print(ans)