#https://www.acmicpc.net/problem/1697
from collections import deque

N,K = map(int,input().split())

road = [0 for _ in range(200001)]

def isValid(n) :
    if 0<=n<=100000 :
        return True
    else :
        return False

def bfs() :
    q = deque()
    q.append(N)
    road[N] = 1
    while q :
        k = q.popleft()
        if k == K :
            break
        for i in range(3) :
            if i == 0 :
                nx = k+1
            elif i == 1:
                nx = k-1
            elif i == 2 :
                nx = k*2

            if isValid(nx) and road[nx] == 0 :
                road[nx] = road[k] + 1
                q.append(nx)

bfs()
print(road[K]-1)



