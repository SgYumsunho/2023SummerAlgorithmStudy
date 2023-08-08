#https://www.acmicpc.net/problem/11403
#경로찾기
from collections import deque
n = int(input())

visit = [[0 for j in range(n)] for i in range(n)]
graph = []

for i in range(n) :
    data = list(map(int,input().split()))
    graph.append(data)

def bfs(x) :
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue :
        q = queue.popleft()
        for i in range(n) :
            if check[i] == 0 and graph[q][i] == 1 :
                queue.append(i)
                check[i] = 1
                visit[x][i] = 1

for i in range(n) :
    bfs(i)

for i in range(n) :
    for j in range(n) :
        print(visit[i][j],end = " ")
    print()




