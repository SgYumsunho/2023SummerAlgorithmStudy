def solution(participant, completion):
    answer = ''
    dict = {}
    for people in participant : 
        if people not in dict.keys() : 
            dict[people] = 1
        else : 
            dict[people] += 1
        
    for people in completion : 
        dict[people] -= 1
    
    
    for people in dict.keys() : 
        if dict[people] != 0 : 
            answer += people
            break
            
    
    return answer