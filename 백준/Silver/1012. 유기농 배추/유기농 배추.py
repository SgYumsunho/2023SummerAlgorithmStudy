#https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10000)
#dfs
def dfs(x,y) :
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<m) and (0<=ny<n) :
            if field[ny][nx] == 1 :
                field[ny][nx] = 0
                dfs(nx,ny)

#테스트 케이스 숫자
T = int(input())

for i in range(T) :
    m,n,k = map(int,input().split())
    count = 0
    # field 초기화
    field = [[0 for _ in range(m)] for _ in range(n)]
    #field에 배추 있으면 1, 없으면 0
    for i in range(k) :
        a,b = map(int,input().split())
        field[b][a] = 1

    for i in range(m) :
        for j in range(n) :
            if field[j][i] == 1 :
                dfs(i,j)
                count += 1
    print(count)

