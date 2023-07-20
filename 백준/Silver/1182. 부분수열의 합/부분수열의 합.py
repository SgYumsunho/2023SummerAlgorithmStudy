#https://www.acmicpc.net/problem/1182

n,s = map(int,input().split())
data = list(map(int,input().split()))
answer = 0

def solve(subset_sum,idx,cnt) :
    global answer,s
    if s == subset_sum and cnt > 0:
        answer += 1
    for i in range(idx,n) :
        solve(subset_sum + data[i],i+1,cnt+1)
#이전거를 넣고 안넣고로 complete binary tree를 만들면 될 것 같음
solve(0,0,0)
print(answer)