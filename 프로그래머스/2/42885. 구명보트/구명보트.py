def solution(people, limit):
    from collections import deque
    people.sort()
    people = deque(people)
    answer = 0
    while people :
        if len(people) == 1 : 
            answer += 1
            break
        else : 
            if people[0] + people[-1] > limit : 
                people.pop()
                answer += 1
            else : 
                people.popleft()
                people.pop()
                answer += 1
                
    return answer