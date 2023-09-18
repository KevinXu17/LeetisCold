def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # z, o, t = 0, 0, 0
    # for n in nums:
    #     if n == 0:
    #         z = z + 1
    #     elif n == 1:
    #         o = o + 1
    #     else:
    #         t = t + 1
    # for r in range(z):
    #     nums[r] = 0
    # for r in range(z, z + o):
    #     nums[r] = 1
    # for r in range(z + o, z + o + t):
    #     nums[r] = 2

    ## 3 pointer
    ## left pivot right   (TODO slow since if first lots of 1 then we need to swarp 1 and 0 a lot)
    # l, p, r = -1, 0, len(nums) + 1
    # while p < r:
    #     if nums[p] == 0:
    #         l = l + 1
    #         nums[p] = nums[l]
    #         nums[l] = 0
    #         p = p + 1
    #     elif nums[p] == 1:
    #         p = p + 1
    #     else:
    #         r = r - 1
    #         nums[p] = nums[r]
    #         nums[r] = 2

    ## TODO Counter
    from collections import Counter
    counts = Counter(nums)
    total_0 = counts[0]
    for i in range(total_0):
        nums[i] = 0
    total_1 = counts[1]
    for i in range(total_0, total_0 + total_1):
        nums[i] = 1
    total_2 = counts[2]
    for i in range(total_0 + total_1, total_0 + total_1 + total_2):
        nums[i] = 2

