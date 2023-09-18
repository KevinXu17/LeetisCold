## TODO same as overlap; if overlap count 0; otherwise 1

def findMinArrowShots(points):
    points.sort(key=lambda x: x[1])
    res = 1
    pivot = points[0]
    for b in points[1:]:
        if b[0] <= pivot[1]:
            continue
        res += 1
        pivot = b
    return res
