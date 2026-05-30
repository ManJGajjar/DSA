from typing import List 

arr = [9,2,8,3,7,6]

def bubble_sort (arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr
    
print(bubble_sort(arr))