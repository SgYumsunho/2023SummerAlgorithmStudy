def solution(sequence) :
    
    def pulse(arr) :
        s1,s2 = [], []
        pulse = 1
        for i in sequence :
            s1.append(pulse*i)
            pulse *= -1
            s2.append(pulse*i)    
        return [s1,s2]
    
    def max_prefix(arr) :
        prefix = [0]
        for i in arr:
            prefix.append(max(0, prefix[-1]) + i)
        return max(prefix)
    
    s1,s2 = pulse(sequence)
    answer = max(max_prefix(s1), max_prefix(s2))
    return answer