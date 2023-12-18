# https://leetcode.com/problems/top-k-frequent-elements/description/
from typing import List
from collections import Counter
import heapq

'''
    build in Counter => heapq
'''
def topKFrequent(nums: List[int], k: int) -> List[int]:
    if k == len(nums):
        return nums
    counter = Counter(nums)
    # return heapq.nlargest(k, counter.keys(), key=counter.get)
    return [values[0] for values in counter.most_common(k)]

'''
    Counter => quick search => topKFrequent
'''