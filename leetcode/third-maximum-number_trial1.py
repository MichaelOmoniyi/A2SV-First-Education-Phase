from collections import Counter
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numsCount = Counter(nums)
        numsCountSorted = sorted(numsCount.items())

        if len(numsCountSorted) >= 3:
            return(numsCountSorted[-3][0])
        else:
            return(max(numsCountSorted)[0])