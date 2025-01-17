def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    nums = [6, 4, 8, 1, 10, 5, 6, 9]
    print(nums)
    nums = quick_sort(nums)
    print(nums)
