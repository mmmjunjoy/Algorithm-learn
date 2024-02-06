
# 정확도 70 %,
# 효율성 0 %


# remove 사용 

def solution1(scoville, K):

 
    # 모든 원소가 k 보다 작은지 체크하기
    index = 0
    count = 0
    for i in range(1,len(scoville)):
            if scoville[index] < K:
                #remove() - '값'으로 접근하여 원소를 삭제한다
                mostmin = min(scoville)
                scoville.remove(mostmin)
                moremin = min(scoville)
                newitem = mostmin + (moremin*2)
                
                scoville.append(newitem)
                scoville.remove(moremin)
                count+=1

                print(scoville)
            else:
                index +=1
    print(scoville)
    print("count",count)

    return count



# pop 사용


def solution2(scoville, K):

    scoville.sort()
    count = 0
    print(scoville)
    for i in scoville:
         
        if i < K:
            print("섞자")
            a = scoville.pop(0)
            b = scoville.pop(0)
            c = a + (b*2)
            scoville.append(c)
            scoville.sort()
            count+=1
            
    
    print(count)
    return count