#https://www.acmicpc.net/problem/2343
def return_cnt(mid,length) :
    cnt = 0
    temp = 0
    for i in range(len(length)) :
        if temp + length[i] > mid :
            cnt +=1
            temp = 0
        temp += length[i]
    else :
        if temp :
            cnt += 1
    return cnt

n,m = map(int,input().split())
length = list(map(int,input().split()))

left = max(length)
right = sum(length)
cnt = 0
temp = 0
i = 0
while left <= right :
    cnt = 0
    mid = (left + right) // 2
    cnt = return_cnt(mid,length)
    if cnt > m :
        left = mid + 1
    elif cnt <= m :
        right = mid-1

print(left)

