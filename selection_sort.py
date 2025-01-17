def selection_sort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        temp = nums[i]
        nums[i] = nums[smallest]
        nums[smallest] = temp

if __name__ == '__main__':
    nums = [6, 4, 8, 1, 10, 5, 6, 9]
    print(nums)
    selection_sort(nums)
    print(nums)
