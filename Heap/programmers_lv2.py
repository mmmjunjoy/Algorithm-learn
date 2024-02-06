
# 정확도 70 %,
# 효율성 0 %


def solution(scoville, K):

 
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