#https://www.acmicpc.net/problem/2212

# 센서 갯수
n = int(input())
# 기지국 개수
k = int(input())
sensors = list(map(int,input().split()))
distances = []
sensors.sort()
for i in range(len(sensors)-1) :
    distances.append(sensors[i+1]-sensors[i])

distances.sort()
sum = 0
for i in range(len(distances)-(k-1)) :
    sum += distances[i]

print(sum)