def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    else:
        mid = (low + high) // 2
        min1, max1 = find_min_max(arr, low, mid)
        min2, max2 = find_min_max(arr, mid+1, high)
        return min(min1, min2), max(max1, max2)

arr = list(map(int, input("Enter elements of the array: ").split()))
min_val, max_val = find_min_max(arr, 0, len(arr) - 1)
print("Minimum value:", min_val)
print("Maximum value:", max_val)
