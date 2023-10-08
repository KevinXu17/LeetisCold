## https://leetcode.com/problems/house-robber/description/

## DP
def rob(nums):
    mem = {}
    mem[0] = nums[0]
    if len(nums) == 1:
        return nums[0]
    mem[1] = max(nums[0], nums[1])

    def helper(i):
        if i in mem:
            return mem[i]
        res = max(helper(i - 1), helper(i - 2) + nums[i])
        mem[i] = res
        return res

    return helper(len(nums) - 1)


## two pointers
def rob2(nums):
    pre_pre = nums[0]
    if len(nums) == 1:
        return pre_pre
    pre = max(pre_pre , nums[1])
    for i in range(2, len(nums)):
        temp = pre
        pre = max(pre_pre + nums[i], pre)
        pre_pre = temp
    return pre


## diff versioin with circle
## https://leetcode.com/problems/house-robber-ii/description/
## A B C D E F
## the key is A can not work with F; so we have 2 link: A to E and B to F