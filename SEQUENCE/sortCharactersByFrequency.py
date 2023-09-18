

def frequencySort(s: str) -> str:
    bucket = {}
    for n in s:
        if n in bucket:
            bucket[n] = bucket[n] + 1
        else:
            bucket[n] = 1
    chars = [(k, v) for k, v in bucket.items()]
    chars_sort = sorted(chars, key=lambda x: x[1], reverse=True)
    res = []
    for c in chars_sort:
        k, i = c
        res = res + [k] * i
    print(res)

s = 'aabbbbbe'
frequencySort(s)

## TODO
## python Counter library
# class Solution:
#     def frequencySort(self, s: str) -> str:
#           import collections
#         # create Counter object from characters in s
#         counts = Counter(s)
#
#         # build result string
#         res = ""
#         for char, count in counts.most_common():
#             res += char * count
#
#         return res