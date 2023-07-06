#사과담기게임
#https://www.acmicpc.net/problem/2828

a = list(map(int,input().split()))
L = a[0]
M = a[1]
apples = list()
num = int(input())

for i in range(num) :
    n = int(input())
    apples.append(n)

bag_min = 1
bag_max = bag_min + M -1

distance = 0
for i in range(num) :
    if apples[i] >= bag_min and apples[i] <= bag_max :
        distance += 0
    elif apples[i] > bag_max :
        distance += apples[i] - bag_max
        bag_max = apples[i]
        bag_min = apples[i] - M + 1
    elif apples[i] < bag_min :
        distance += bag_min - apples[i]
        bag_min = apples[i]
        bag_max = apples[i] + M -1
    else :
        continue

print(distance)