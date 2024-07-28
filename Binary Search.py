def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid, comparisons
    return -1, comparisons
arrays = [
    ([5, 10, 15, 20, 25, 30, 35, 40, 45], 20, 4),
    ([10, 20, 30, 40, 50, 60], 50, 5),
]

for arr, key, expected in arrays:
    print(f"Array: {arr}, Search Key: {key}")
    index, comparisons = binary_search(arr, key)
    print(f"Expected Index: {expected}, Output Index: {index}, Comparisons: {comparisons}\n")
