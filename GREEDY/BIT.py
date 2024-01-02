'''
    Binary index tree: get sum from random range
    update/get_sum O(logn)
'''
n = 8
BIT = [0] * (n + 1)


def update(x, v):
    i = x
    while i <= n:
        BIT[i] += v
        i += (i & -i)


def get_sum(x):
    i = x
    sum = 0
    while i > 0:
        sum += BIT[i]
        i -= (i & -i)
    return sum

update(5, 1)
update(4, 1)

# for b in BIT:
#     print(b)
print(get_sum(6))