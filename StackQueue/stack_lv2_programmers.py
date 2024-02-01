
# 푸는 과정


# 각 작업당, 얼만큼의 일수가 소요되는지 까지 , list 생성



def solution(progresses, speeds):
    
    result = 100
    lens = len(progresses)
    
    resultlist =[]
    
    for i in range(lens):
        middle = result - progresses[i]
        print("mid",middle)
#         // - 몫
#          % - 나머지
        
        mok = middle // speeds[i]
        na = middle % speeds[i]
        
        if na>0:
            mok=mok+1
        
        resultlist.append(mok)
        
        
    
    return resultlist