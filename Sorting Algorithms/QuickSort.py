from typing import List
import random

arr = [45, 30, 29, 19, 50, 1]

def quick_sort_random_pivot(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Randomly select a pivot and swap it with the last element
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        # Partition the array and get the pivot's final index
        pivot_index = _partition(arr, low, high)

        # Recursively sort elements before and after the pivot
        quick_sort_random_pivot(arr, low, pivot_index - 1)
        quick_sort_random_pivot(arr, pivot_index + 1, high)

    return arr

def _partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]  
    i = low - 1        

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

def quick_sort(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = _partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

    return arr

print(quick_sort(arr.copy())) 
print(quick_sort_random_pivot(arr.copy()))  