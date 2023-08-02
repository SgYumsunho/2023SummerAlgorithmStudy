#https://www.acmicpc.net/problem/1189

n,m,depth = map(int,input().split())
graph = [list(input()) for _ in range(n)]
result = 0

def solve(x,y,k) :
    global result
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    if k == depth :
        if x == 0 and y == m-1 :
            result += 1
    else :
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 'T' :
                graph[nx][ny] = 'T'
                solve(nx,ny,k+1)
                graph[nx][ny] = '.'


graph[n-1][0] = 'T'
solve(n-1,0,1)
print(result)
