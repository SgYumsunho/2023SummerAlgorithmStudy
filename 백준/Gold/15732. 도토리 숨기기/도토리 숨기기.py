#https://www.acmicpc.net/problem/15732

from collections import deque
MAX_INT = 10000000
n,k,d = map(int,input().split())
left,right = 0,n
rules = []
cnt = 0

for _ in range(k) :
    start,end,step = map(int,input().split())
    rules.append((start,end,step))

def calc(rules,mid) :
    cnt = 0
    for left,right,step in rules :
        if mid < left :
            continue
        right = min(mid,right)
        cnt += (right - left) // step + 1
    return cnt

def bs(rules,right,d) :
    left = 0
    while left <= right :
        mid = (left+right) // 2
        corn = calc(rules,mid)
        if corn < d :
            left = mid + 1
        else :
            right = mid - 1
    return left


print(bs(rules,right,d))


