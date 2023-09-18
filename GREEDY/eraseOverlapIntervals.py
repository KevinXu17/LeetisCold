def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    res = 0
    pivot = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[pivot][1]:
            res += 1
        else:
            pivot = i
    return res



ints = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(eraseOverlapIntervals(ints))
