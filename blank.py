# public int binarySearch(int[] nums, int key) {
#     int l = 0, h = nums.length;
#     while (l < h) {
#         int m = l + (h - l) / 2;
#         if (nums[m] >= key) {
#             h = m;
#         } else {
#             l = m + 1;
#         }
#     }
#     return l;
# }

def binarySearch(nums, key):
    l = 0
    h = len(nums)
    while (l < h):
        m = l+(h-l)//2
        if nums[m] >= key:
            h = m
        else:
            l = m + 1
    return l


nums = []
key = 1
print(binarySearch([1,1,1], 1))