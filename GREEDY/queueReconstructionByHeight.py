## Since X[1] is affected by the larger number ahead, we can ignore the smaller one and put them ahead
## TODO so sort by largest then according the X[1]
# https://leetcode.com/problems/queue-reconstruction-by-height/description/

def reconstructQueue(people):
    output = []
    people.sort(key=lambda x: (-x[0], [1]))
    for x in people:
        output.insert(x[1], x)
    return output


"""
    greedy with shorter ppl and let them stand first
    Binary index tree: update how many people ahead
    BIT: update: find the last 1 and add 1 ot it => i += (i&-i)
           100          110
            4            6
       010    011    101
        2      3      5
    001
     1
     get_sum: sub the last 1 with 1 => i -= (i&-i)
     e.g: get sum from 5: we need to add value at 5 and 4
     001       010       100
      1         2         4
            011        101  110
             3          5    6
"""
def reconstructQueue2(people):
    n = len(people)
    BIT = [0] * (n + 1)
    def update(x, v):
        i = x
        while i <= n:
            BIT[i] += v
            i += (i&-i)

    def get_sum(x):
        i = x
        sum = 0
        while i > 0:
            sum += BIT[i]
            i -= (i&-i)
        return sum

    output = [[0,0]] * n
    people.sort(key=lambda x: (x[0], -x[1]))
    for i in range(2, n+1):
        update(i, 1)
    for i in range(n):
        b = 0
        e = n
        while b < e:
            mid = b + (e - b) // 2
            new_seat = get_sum(mid + 1)
            if new_seat < people[i][1]: b = mid + 1
            else: e = mid # need to zip the same # new_seat since have 0 seat update

        output[b] = people[i]
        update(b+1, -1)
    return output

res = reconstructQueue2([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
for r in res:
    print(r)