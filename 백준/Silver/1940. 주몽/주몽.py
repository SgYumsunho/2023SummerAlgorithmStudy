#https://www.acmicpc.net/problem/1940

n = int(input())
target = int(input())
weight = list(map(int,input().split()))

weight.sort()

left, right = 0,len(weight)-1
count = 0

while left < right :
    sum = weight[left] + weight[right]
    if sum < target :
        left += 1
    elif sum > target :
        right -= 1
    else :
        count +=1
        left += 1
        right -= 1

print(count)

