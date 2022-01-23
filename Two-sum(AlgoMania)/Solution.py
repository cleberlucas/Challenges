def solution(numbers, target_sum):   
    for i,p in enumerate(numbers):
        ress = target_sum - p
        if (ress in numbers and numbers.index(ress)!=i):
            return sorted([ress, p] )  
    return []
