#거스름돈
#https://www.acmicpc.net/problem/14916

change = int(input())
cnt1 = 0
cnt2 = 0

while 1 :
    if change % 5 == 0 :
        cnt1 += change // 5
        change = 0
    else :
        change -= 2
        cnt2 += 1
    if change == 0 :
        print(cnt1+cnt2)
        break
    if change < 0 :
        print(-1)
        break
