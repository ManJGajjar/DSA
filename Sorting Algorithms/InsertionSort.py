from typing import List

arr = [9,2,5,6,3,1]

def insertion_sort(arr: List[int]) -> List[int]:
    for i in range (1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key

    return arr

print(insertion_sort(arr))