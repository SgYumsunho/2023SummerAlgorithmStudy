from collections import deque
import sys
input = sys.stdin.readline
n, m, p = map(int, input().split())
s = [[] for i in range(m + 1)] # 요소 탐색을 위한 그래프를 만들어준다.
visit = [[] for i in range(m + 1)] # 방문을 체크하기 위해 visit 배열을 만들어준다.
for i in range(n): # n만큼 요소를 넣어 그래프들을 초기화 해준다.
    a, b = map(int, input().split())
    s[b].append(a)
    visit[b].append(0)
def dfs(start): 
    q = deque() # 연결 그래프를 검사하기 위한 큐를 만든다.
    q.append(start) # 처음 que 값을 집어넣고
    cnt = 0 # 갯수를 기록할 변수 초기화
    while q: # 큐에 요소가 없을때 까지 반복
        st = q.popleft() # 큐에 있는 값을 꺼내서 (start값)
        for i in range(len(s[st])): # 그래프 요소 수만큼 반복
            if s[st][i] != 0 and visit[st][i] == 0: # 아직 방문하지 않았고 그래프가 연결 되어 있으면
                q.append(s[st][i]) # que에 추가
                visit[st][i] = 1 # 방문 처리
                cnt += 1 # 갯수 하나 추가
                break
            if visit[st][i] == 1: # 이미 방문했을 경우 (순환그래프일 경우) -1을 반환
                return -1
    return cnt
print(dfs(p)) # p부터 시작