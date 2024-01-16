## https://leetcode.com/problems/partition-labels/description/

"""
    each char has a range: check whether it has char in range over range
"""

def partitionLabels(s):
    reversed_index = {}
    res = []
    for i in range(len(s)):
        if s[i] in reversed_index:
            reversed_index[s[i]][1] = i
        else:
            reversed_index[s[i]] = [i, i]
    ranges = list(reversed_index.values())
    rg = ranges[0][1]
    pivot = 0
    l = ranges[0][0]
    res.append(1)
    print(ranges)
    for i in range(1, len(ranges)):
        if ranges[i][0] <= rg:
            rg = max(ranges[i][1], rg)
        else:
            res[pivot] = rg - l + 1
            pivot += 1
            l = ranges[i][0]
            res.append(1)
            rg = ranges[i][1]
    res[pivot] = rg - l + 1
    return res

def partitionLabels2(s: str):
    # char begin_position
    char_position = {}
    # idx begin_position, value end_position
    list_map = [-1] * len(s)
    for i in range(len(s)):
        if s[i] in char_position:
            list_map[char_position[s[i]]] = i
        else:
            char_position[s[i]] = i
        list_map[i] = i
    res = []
    i = 0
    while i < len(list_map):
        j = list_map[i]
        rg = max(list_map[i:j + 1])
        # push to maximum range
        while rg > j:
            temp = j
            j = rg
            rg = max(list_map[temp:j + 1])

        res.append(rg - i + 1)
        i = rg + 1
    return res
print(partitionLabels2("ababcbacadefegdehijhklij"))



