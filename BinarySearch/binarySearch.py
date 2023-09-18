## find the index of the key

## just find the index
def binarySearch(nums, key):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == key:
            return m
        elif nums[m] > key:
            r = m - 1
        else:
            l = m + 1
    return -1

## if multiple num in nums, fine the smallest index
def binarySearch2(nums, key):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] >= key:
            r = m - 1
        else:
            l = m + 1
    return l



