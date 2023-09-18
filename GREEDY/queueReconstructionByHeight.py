## Since X[1] is affected by the larger number ahead, the largest one must with 0 in X[1]
## TODO so sort by largest then according the X[1]


def reconstructQueue(people):
    output = []
    people.sort(key=lambda x: (-x[0], [1]))
    for x in people:
        output.insert(x[1], x)
    return output


