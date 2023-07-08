#https://www.acmicpc.net/problem/20300
N = int(input())
data  = list(map(int,input().split()))
data = sorted(data)
result = []
if N % 2 == 0 :
    for i in range(int(N/2)) :
        result.append(data[i] + data[len(data)-1-i])
else :
    for i in range(int(N/2)) :
        result.append(data[i]+data[len(data)-2-i])
    result.append(data[len(data)-1])

print(max(result))