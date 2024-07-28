def binary_search_with_steps(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    steps = []

    while low <= high:
        mid = (high + low) // 2
        steps.append(mid)
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid, steps
    return -1, steps
arrays = [
    ([3, 9, 14, 19, 25, 31, 42, 47, 53], 31, 6),
]

for arr, key, expected in arrays:
    print(f"Array: {arr}, Search Key: {key}")
    index, steps = binary_search_with_steps(arr, key)
    print(f"Expected Index: {expected}, Output Index: {index}, Steps: {steps}\n")
