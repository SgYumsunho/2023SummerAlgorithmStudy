def solution(survey, choices):
    answer = ''
    #survey[0]의 첫번째 캐릭터 -> 1번째 질문에 대한 비동의 관련 선택지 선택시 받는 성격유형
    #survey[0]의 두번째 캐릭터 -> 2번째 질문에 대한 비동의 관련 선택지 선택시 받는 성격유형
    #choices[0] -> 검사자가 선택한 i+1번째 질문의 선택지(1<=n<=7)
    
    character = {"R" : 0 ,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0}
    
    for i in range(len(survey)) : 
        s = list(survey[i])
        s1 = s[0]
        s2 = s[1]
        if choices[i] < 4 : 
            character[s1] += 4 - choices[i]
        else : 
            character[s2] += choices[i] - 4
        
    mbti_keys = list(character.keys())
    
    for left,right in zip(mbti_keys[::2], mbti_keys[1::2]) : 
        if character[left] >= character[right] : 
            answer += left
        else : 
            answer += right
    
    
    return answer