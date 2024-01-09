
## https://leetcode.com/problems/can-place-flowers/submissions/903724232/

def canPlaceFlowers(flowerbed, n):
    # res = False
    # current = 0
    # pivot = 0
    # end = len(flowerbed) - 1
    # while pivot <= end:
    #     # 0 pivot
    #     if flowerbed[pivot] == 0:
    #         if pivot + 1 <= end:
    #             if flowerbed[pivot + 1] == 0:
    #                 current += 1
    #                 pivot += 2
    #             else:
    #                 pivot += 3
    #         else:
    #             if pivot - 1 > 0 and flowerbed[pivot - 1] == 0:
    #                 current += 1
    #                 pivot += 2
    #             else:
    #                 current += 1
    #                 break
    #     else:
    #         pivot += 2
    #     if current >= n:
    #         res = True
    #         break
    # return res
## TODO count 3's 0
    # if not n:
    #     return True
    # flowerbed.append(0)
    # count = 1
    # current = 0
    # for i in flowerbed:
    #     if i == 0:
    #         count += 1
    #         if count == 3:
    #             current += 1
    #             if current >= n:
    #                 return True
    #             count = 1
    #     else:
    #         count = 0
    # return False
## TODO check front pivot back
    # add front/end tail
    fb = [0] + flowerbed + [0]
    for i in range(1, len(fb) - 1):
        if fb[i-1] == 0 and fb[i] == 0 and fb[i+1] == 0:
            fb[i] = 1
            n -= 1
        if n <= 0:
            return True
    return False

print(canPlaceFlowers([0], 2))