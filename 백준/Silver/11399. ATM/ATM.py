#https://www.acmicpc.net/problem/11399
n = int(input())
data = list(map(int,input().split()))

data = sorted(data)
result = 0
for i in range(len(data)) :
    for k in range(i+1) :
        result += data[k]

print(result)