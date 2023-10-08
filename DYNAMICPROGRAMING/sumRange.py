class NumArray:

    def __init__(self, nums: List[int]):
        mem = [nums[0]]
        for i in range(1, len(nums)):
            mem.append(mem[i - 1] + nums[i])
        self.mem = mem
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.mem[right]
        return self.mem[right] - self.mem[left - 1]