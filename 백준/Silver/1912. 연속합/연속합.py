#https://www.acmicpc.net/problem/1912

n = int(input())
data = list(map(int,input().split()))

d= [0]*n
d[0] = data[0]

for i in range(1,n) :
    d[i] = max(data[i],d[i-1] + data[i])

print(max(d))

