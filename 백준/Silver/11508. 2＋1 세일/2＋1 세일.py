#https://www.acmicpc.net/problem/11508

n = int(input())
costs = list()
for i in range(n) :
    costs.append(int(input()))

costs = sorted(costs,reverse=True)
cnt = 1
result = 0
for i in range(len(costs)) :
    if cnt % 3 == 0 :
        cnt = 1
        continue
    result += costs[i]
    cnt+=1

print(result)