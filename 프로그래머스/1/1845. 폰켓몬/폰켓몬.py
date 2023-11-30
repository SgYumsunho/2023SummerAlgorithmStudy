def solution(nums):
    answer = 0
    half = len(nums) // 2
    pokemon = {}
    
    for num in nums : 
        if num not in pokemon : 
            pokemon[num] = 1
        else : 
            pokemon[num] += 1
            
    
    if len(pokemon.keys()) >= half : 
        answer = half
    else : 
        answer = len(pokemon.keys())
    
    
    return answer