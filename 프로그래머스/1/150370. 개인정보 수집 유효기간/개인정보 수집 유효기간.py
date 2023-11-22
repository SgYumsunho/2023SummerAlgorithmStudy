def solution(today, terms, privacies):
    from datetime import datetime,timedelta
    from dateutil.relativedelta import relativedelta
    
    answer = []
    new_terms = {} #약관종류, 유효기간
    today_date = datetime.strptime(today, '%Y.%m.%d')
    
    for i in range(len(terms)) : 
        yakgwan, validDate = terms[i].split()
        validDate = int(validDate)
        if yakgwan not in new_terms.keys() : 
            new_terms[yakgwan] = validDate
            
    for i in range(len(privacies)) :
        date, yakgwan = privacies[i].split() #개인정보 수집 일자, 약관종류
        validMonth = new_terms[yakgwan]
        record_date = datetime.strptime(date, "%Y.%m.%d")
        limit = record_date + relativedelta(months=validMonth)
        
        #print(limit)
        
        if limit <=today_date :
            answer.append(i+1)
    
        
            
    return answer