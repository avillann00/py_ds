def bin_search(arr, val):
    low, high = 0, len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def bin_search_recursive(arr, val, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == val:
        return mid
    elif arr[mid] > val:
        high = mid - 1
    else:
        low = mid + 1

    return bin_search_recursive(arr, val, low, high)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(bin_search(array, 6))
print(bin_search_recursive(array, 6, 0, len(array)))
