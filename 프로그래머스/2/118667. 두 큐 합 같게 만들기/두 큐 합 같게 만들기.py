from collections import deque

def solution(queue1, queue2):
    answer = -2
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    t1 = sum(queue1)
    t2 = sum(queue2)
    
    
    if ((t1 + t2) % 2 != 0) :
        answer = -1
        return answer
    
    target = (t1 + t2) // 2
    cnt = 0
    
    
    while(True) : 
        
        if t1 == t2 : 
            answer = cnt
            return answer
        if t1 > t2 : 
            t = q1.popleft()
            q2.append(t)
            t1 -= t
            t2 += t
            cnt += 1
            #print(t1,t2)
        else : 
            t = q2.popleft()
            q1.append(t)
            cnt += 1
            t1 += t
            t2 -= t
            #print(t1,t2)
        
        if cnt >= len(queue1) * 3 : 
            return -1
        
    return answer