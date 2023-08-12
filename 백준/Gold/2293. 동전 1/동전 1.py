#https://www.acmicpc.net/problem/2293

n,k = map(int,input().split())
costs = []
for i in range(n) :
    costs.append(int(input()))

dp = [0 for i in range(k+1)]
dp[0] = 1

for cost in costs :
    for j in range(cost,k+1) :
        if j - cost >= 0 :
            dp[j] += dp[j-cost]

print(dp[k])


