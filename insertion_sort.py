def insertion_sort(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            for j in range(i, 0, -1):
                if nums[j] > nums[j - 1]:
                    break
                temp = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = temp

if __name__ == '__main__':
    nums = [6, 4, 8, 1, 10, 5, 6, 9]
    print(nums)
    insertion_sort(nums)
    print(nums)
