"""
    swarp the adjacent elements until the end;
    each run will put the largest one to the end;
    3 9 1 2 5 6
              P
    3 1 2 5 6 9 (first round)
            P
    1 2 3 5 6 9 (second round)

    Time: O(n^2)

"""

def bubbleSort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums
