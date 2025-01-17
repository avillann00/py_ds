def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

if __name__ == '__main__':
    nums = [6, 4, 8, 1, 10, 5, 6, 9]
    print(nums)
    bubble_sort(nums)
    print(nums)
