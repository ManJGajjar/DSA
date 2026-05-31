from typing import List

arr = [5,3,8,1,2]

def selection_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort(arr))