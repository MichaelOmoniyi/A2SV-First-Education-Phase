class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numCount = {}
        maxOperation = 0

        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1

        for num in nums:
            complement = k - num
            if complement in numCount:
                if numCount[num] > 0:
                    numCount[num] -= 1
                    numCount[complement] -= 1
                    if numCount[num] >= 0 and numCount[complement] >= 0:
                        maxOperation += 1
        return maxOperation