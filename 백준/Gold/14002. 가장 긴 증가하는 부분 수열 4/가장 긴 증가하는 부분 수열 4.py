#https://www.acmicpc.net/problem/14002

n = int(input())
data = list(map(int,input().split()))
dp = [1 for _ in range(n)]


for i in range(n) :
    for j in range(i) :
        if data[i] > data[j] :
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

max_dp = max(dp)
result = []
for i in range(n-1,-1,-1) :
    if dp[i] == max_dp :
        result.append(data[i])
        max_dp -= 1

result.reverse()
for i in result :
    print(i,end = " ")