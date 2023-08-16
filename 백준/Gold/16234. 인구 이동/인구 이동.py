#https://www.acmicpc.net/problem/16234
from collections import deque
import math


n,left,right = map(int,input().split())
graph = []
visited = [[False]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(n) :
    graph.append(list(map(int,input().split())))

def isValid(x,y) :
    if 0<=x<n and 0<=y<n :
        return True
    else :
        return False

def bfs(i,j) :
    q = deque()
    q.append([i,j])
    visited[i][j] = 1
    cnt = graph[i][j] # 총 연합된 국가 수
    #연합인 국가 담기
    union = [(i,j)]

    # while 문장을 거치면 문이 열려있는 애들을 알 수 있음
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx,ny) and visited[nx][ny] == 0 :
                if left <= abs(graph[x][y] - graph[nx][ny]) <= right :
                    union.append((nx,ny))
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    cnt += graph[nx][ny]

    #이제 연합인 애들을 찾아서 처리해야함.
    for x,y in union :
        graph[x][y] = math.floor(cnt/len(union))

    return len(union)

result = 0 # 인구 이동이 발생하는 일수
while 1 :
    visited = [[False]*n for _ in range(n)]
    flag = False

    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == False :
                if bfs(i,j) > 1 :
                    flag = True
    if flag == False :
        break
    result += 1

print(result)


