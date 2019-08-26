# https://leetcode.com/problems/permutation-sequence/

import math

def getPermutation(n, k):
    nums = [ str(i) for i in range(1, n + 1) ]
    return _getPermutation(nums, k - 1)

def _getPermutation(numbers, k):
    if len(numbers) == 1:
        return numbers[0]

    zone_size = math.factorial(len(numbers) - 1)
    zone_num = k // zone_size
    next_numbers = numbers[:zone_num] + numbers[zone_num+1:]
    return numbers[zone_num] + _getPermutation(next_numbers, k - (zone_num * math.factorial(len(numbers) - 1)))

print(getPermutation(4, 11))
