#https://www.acmicpc.net/problem/19941
#식탁 길이 N, 선택할 수 있는 거리 K, 햄버거 먹을 수 있는 최대 사람 수

N,K = input().split()
N = int(N)
K = int(K)

data = input()
visited = []
cnt = 0
stat = 0

for i in range(N) :
    if data[i] == "H" :
        visited.append(0)
    else :
        visited.append(1)

for i in range(N) :
    if data[i] == "P" :
        #좌측 제일 먼것을 먹어야함
        for j in range(K,0,-1) :
            if i-j >= 0 :
                if visited[i-j] == 0 :
                    visited[i-j] = 1
                    cnt += 1
                    stat = 1
                    break
        #우측 제일 가까운 것을 먹어야함.
        if stat == 0 :
            for j in range(1,K+1) :
                if i+j < len(data) :
                    if visited[i+j] == 0 :
                        visited[i+j] = 1
                        cnt += 1
                        break
        stat = 0

print(cnt)