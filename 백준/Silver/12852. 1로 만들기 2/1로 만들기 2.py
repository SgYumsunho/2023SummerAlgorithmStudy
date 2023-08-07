#https://www.acmicpc.net/problem/12852
n = int(input())
temp = n
dp = [i for i in range(n+1)]
dp[1] = 0
answer = [i for i in range(n+1)]
answer[1] = 0

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    answer[i] = i-1
    if i % 3 == 0 and dp[i] > dp[i//3] +1:
        dp[i] = dp[i//3] + 1
        answer[i] = i//3
    if i % 2 ==0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        answer[i] = i//2

print(dp[n])
print(temp,end=" ")

while answer[temp] != 0 :
    print(answer[temp],end=" ")
    temp = answer[temp]

# 시간초과 난 코드
# while True :
#     if temp%3 == 0 :
#         if dp[temp-1] < dp[temp//3] :
#             temp = temp -1
#         else :
#             temp = temp // 3
#         print(temp, end = " ")
#     elif temp%2 == 0 :
#         if dp[temp-1] < dp[temp//2] :
#             temp = temp -1
#         else :
#             temp = temp // 2
#         print(temp, end = " ")
#     if temp == 1 :
#         break

