# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

def reverseVowels(s: str) -> str:
    begin = 0
    end = len(s) - 1
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = list(s)
    while begin < end:
        if res[begin].lower() in vowels:
            if res[end].lower() in vowels:
                temp = res[begin]
                res[begin] = res[end]
                res[end] = temp
                end = end - 1
                begin = begin + 1
            else:
                end = end - 1
        else:
            begin = begin + 1
    return "".join(res)