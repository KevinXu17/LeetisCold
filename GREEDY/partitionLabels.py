## https://leetcode.com/problems/partition-labels/description/


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

print(partitionLabels("bbvemgjwruuwalp"))



