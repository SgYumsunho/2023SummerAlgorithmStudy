#https://www.acmicpc.net/problem/1092
import heapq

n = int(input())
cranes = list(map(int,input().split()))

m = int(input())
boxes = list(map(int,input().split()))

cranes.sort(reverse = True)
boxes.sort(reverse = True)

time = 0

if boxes[0] > cranes[0] :
    print(-1)
    exit()
else :
    while len(boxes) > 0 :
        for i in range(len(cranes)):
            for j in range(len(boxes)):
                if cranes[i] >= boxes[j]:
                    boxes.pop(j)
                    break
        time += 1
print(time)



