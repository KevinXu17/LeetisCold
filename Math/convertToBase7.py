# https://leetcode.com/problems/base-7/description/

def convertToBase7(num: int) -> str:
    if num == 0: return '0'
    sign = '' if num > 0 else '-'
    temp = -num if num < 0 else num
    base7 = ''
    while temp > 0:
        base7 = str(temp % 7) + base7
        temp = temp // 7
    return sign + base7


# https://leetcode.com/problems/convert-a-number-to-hexadecimal/submissions/
def toHex(num: int) -> int:
    hexMap = '0123456789abcdef'
    if num == 0: return '0'
    res = ''
    for i in range(8):
        r = hexMap[num & 0xf]
        res = r + res
        num = num >> 4
    return res.lstrip('0')