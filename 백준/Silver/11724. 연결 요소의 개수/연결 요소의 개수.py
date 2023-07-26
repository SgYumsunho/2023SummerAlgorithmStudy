#https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(10000)

def dfs(graph, node, visited) :
    visited[node] = True
    # 한바퀴 다 돌면 i번 노드에 대해 연결된 것들이 다 T로 바뀜
    # dfs 함수 호출이 끝날때 cnt + 1
    for i in graph[node] :
        if not visited[i] :
            dfs(graph,i,visited)


n, m = map(int,input().split())
graph = [[i] for i in range(n+1)]
for i in range(m) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)
#[[0], [1, 2, 5], [2, 1, 5], [3, 4], [4, 3, 6], [5, 2, 1], [6, 4]]

visited = [False]*(n+1)
cnt = 0

for i in range(1, n+1) :
    if not visited[i] :
        cnt += 1
        dfs(graph, i , visited)
print(cnt)


