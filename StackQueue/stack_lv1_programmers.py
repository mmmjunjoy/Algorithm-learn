# 위 코드는 정확도 100 ,  효율성 0 -> 시간초과

# programmers - 같은 숫자는 싫어 

def solution(arr):
    
    i = 0
    lens = len(arr)
    for _ in range(0,lens-1):
        if arr[i] != arr[i+1]:
            i+=1
        else:
            arr.pop(i)
        
        
    print('Hello Python')
    return arr