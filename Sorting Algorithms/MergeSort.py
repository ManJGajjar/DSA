from typing import List 

arr = [45,30,29,19,50,1]

def merge_sort (arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    #DIVIDE
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    #CONQUER
    return _merge(left, right)

def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if  left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(merge_sort(arr))