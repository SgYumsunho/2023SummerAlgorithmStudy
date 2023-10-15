def solution(sequence) :
    answer = 0
    n = len(sequence)
    dp = [0] * n
    dp[0] = sequence[0]
    # 누적합
    # 0 1 2 3 4 5 6 
    # dp[0] -> 0번째까지의 값으로 만들수 있는 합
    # dp[4] -> 4번째까지의 원소로 만들 수 있는 합
    # 그 중 최댓값
    if n == 1 : 
        answer = max(sequence[0], sequence[0]*-1)
    else : 
        #1 -1 1 -1 ...
        for i in range(1,n,2) : 
            sequence[i] *= -1
        dp[0] = sequence[0] 
        for i in range(1,n) : 
            dp[i] = max(sequence[i], sequence[i] + dp[i-1])
        answer = max(dp)
        
        for i in range(n) : 
            sequence[i] *= -1
            
        dp[0] = sequence[0]
        for i in range(1,n) : 
            dp[i] = max(sequence[i], sequence[i] + dp[i-1])
        
        answer = max(answer, max(dp))

        
    return answer