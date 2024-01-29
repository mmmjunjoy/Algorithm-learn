
# 정확성 100 , 효율성 0.0

def solution(participant, completion):
    

    result = []
    startlen = len(completion)
    
    
    for i in range(startlen):
        if completion[i] in participant:
            d = participant.index(completion[i])
            participant.pop(d)
    
    print("마지막 남은 사람" , participant)
        
    result = participant[0]
    
            
            
            
            
    answer = ''
    return result