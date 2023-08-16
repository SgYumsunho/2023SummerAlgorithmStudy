#https://www.acmicpc.net/problem/2636
from collections import deque

col, row = map(int,input().split())
cheese = []
for i in range(col) :
    cheese.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,-1,1]
ans = []

def isValid(x,y) :
    if 0<=x<col and 0<=y<row :
        return True
    else :
        return False

def bfs() :
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    cnt = 0
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx,ny) and visited[nx][ny] == 0 :
                if cheese[nx][ny] == 0 :
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                elif cheese[nx][ny] == 1 :
                    cheese[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1

    ans.append(cnt)
    return cnt


time = 0
while 1:
    time +=1
    visited = [[0]*row for _ in range(col)]
    cnt = bfs()
    if cnt == 0 :
        break

print(time-1)
print(ans[len(ans)-2])