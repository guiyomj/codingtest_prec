n, m = map(int, input().split())
idx=0
for i in range(n):
    idx=min(list(map(int, input().split())))

print(idx)