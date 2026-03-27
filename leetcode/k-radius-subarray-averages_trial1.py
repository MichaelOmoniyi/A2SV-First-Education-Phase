class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        divisor = (2 * k) + 1
        n = len(nums)

        if k == 0:
            return nums
        
        if n < divisor:
            return [-1] * n

        avgArr = [-1] * n

        window = sum(nums[:divisor])

        left = 0
        right = divisor - 1
        
        avgArr[k] = window // divisor

        for i in range(k + 1, n - k):
            window -= nums[left]
            left += 1
            right += 1
            window += nums[right]
            avgArr[i] = window // divisor
        return avgArr