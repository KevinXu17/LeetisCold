## find the index of the key
# https://leetcode.com/problems/sqrtx/description/
# but some sqrt may be floor => 8 : 2; so we need to set l - 1
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

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
## it can also choose squeeze left or right

# to left
def binarySearch2(nums, key):
    l = 0
    r = len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] >= key:
            r = m
        else:
            l = m + 1
    return l



