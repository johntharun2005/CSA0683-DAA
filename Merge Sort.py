def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr
arrays = [
    ([31, 23, 35, 27, 11, 21, 15, 28], [11, 15, 21, 23, 27, 28, 31, 35]),
    ([22, 34, 25, 36, 43, 67, 52, 13, 65, 17], [13, 17, 22, 25, 34, 36, 43, 52, 65, 67]),
]
for arr, expected in arrays:
    print(f"Array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Expected: {expected}")
    print(f"Output: {sorted_arr}\n")
