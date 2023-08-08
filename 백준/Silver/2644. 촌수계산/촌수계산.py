#https://www.acmicpc.net/problem/2644

from collections import deque

n = int(input())
node1, node2 = map(int,input().split())
relation = int(input())
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
result = []

#2차원 배열에 서로 연결되어 있는 노드 정보 저장
for i in range(relation) :
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(start_node,num) :
    num += 1
    visited[start_node] = True

    if start_node == node2 :
        result.append(num)

    for i in graph[start_node] :
        if visited[i] == False :
            #print("(%d, %d)" % (i, num))
            dfs(i,num)

dfs(node1,0)

if len(result) == 0 :
    print(-1)
else :
    print(result[0]-1)

