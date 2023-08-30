#https://www.acmicpc.net/problem/1911
import math

N,L = map(int,input().split())
pool = []

for i in range(N) :
    pool.append(list(map(int,input().split())))

pool.sort()
cnt = 0
plank = 0
res = 0

for start,end in pool :
    start = max(start,plank)
    cnt = math.ceil((end-start)/L)
    plank = start + cnt * L
    res += cnt

print(res)







