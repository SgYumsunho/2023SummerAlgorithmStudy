#https://www.acmicpc.net/problem/11047

n,cost = input().split()
n = int(n)
cost = int(cost)
coins = list()

for i in range(n) :
    coins.append(int(input()))

cnt = 0

for i in range(len(coins)-1,-1,-1) :
    if cost // coins[i] == 0 :
         continue
    else :
        cnt += cost//coins[i]
        cost -= coins[i] * (cost // coins[i])
    if cost == 0 :
        break

print(cnt)