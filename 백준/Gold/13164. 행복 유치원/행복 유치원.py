#https://www.acmicpc.net/problem/13164

N,M = map(int,input().split())
height = list(map(int,input().split()))

height.sort()
data = []
for i in range(len(height)-1) :
    data.append(height[i+1]-height[i])

data.sort()
cost = 0

for i in range(N-M) :
    cost += data[i]

print(cost)