n,m = map(int,input().split())
r,c,d = map(int,input().split())
visited = [[False]*m for _ in range(n)]
room = []
for _ in range(n) :
    room.append(list(map(int,input().split())))
cnt = 1

state = 0
#북,동,남,서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#첫 위치 방문처리
visited[r][c] = 1

#후진 불가능하면 끝
while True :
    flag = 0
    # 청소되어있지 않다면 청소
    # if 0<=r<n and 0<=c<m :
    #     if room[r][c] == 0 :
    #         visit[r][c] == True
    #         cnt += 1
    # else :
    #     break
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    for i in range(4) :
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        d = (d+3)%4
        if 0<=nx<n and 0<=ny<m and room[nx][ny] == 0 : # 청소되지 않은 빈 칸이 있을 때
            if visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                cnt +=1
                r = nx
                c = ny
                flag = 1
                break
    if flag == 0 : # 4방향 모두 청소가 되어있을 때
        # 후진했을 때 벽
        # 0 -> 3 -> 2 -> 1
        # 북, 동, 남, 서
        if room[r-dx[d]][c-dy[d]] == 1 :
            print(cnt)
            break
        else :
            r,c = r-dx[d],c-dy[d]
