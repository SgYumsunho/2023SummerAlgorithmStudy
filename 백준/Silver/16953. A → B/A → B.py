#https://www.acmicpc.net/problem/16953

A,B = input().split()
A = int(A)
B = int(B)

cnt = 1
#2를 곱한다, 1을 가장 오른쪽에 추가한다.
while B != A :
    if B < A :
        cnt = -1
        break
    if B%2 == 0 :
        B = B//2
        cnt+=1
    elif B%10 == 1 :
        B = B//10
        cnt +=1
    else :
        cnt = -1
        break


print(cnt)
