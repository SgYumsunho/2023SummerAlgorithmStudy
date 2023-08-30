#https://www.acmicpc.net/problem/5557
n = int(input())
data = list(map(int,input().split()))
result = data[len(data)-1]
dp = [[0 for _ in range(21)] for _ in range(n)]

dp[0][data[0]] = 1

for i in range(1,n-1) :
    for j in range(21) :
        if dp[i-1][j] :
            if 0<=j+data[i]<=20 :
                dp[i][j+data[i]] += dp[i-1][j]
            if 0<=j-data[i]<=20 :
                dp[i][j-data[i]] += dp[i-1][j]

print(dp[n-2][data[-1]])