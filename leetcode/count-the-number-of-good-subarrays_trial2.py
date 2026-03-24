class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = {}
        left, pairs, result = 0, 0, 0

        for right in range(len(nums)):
            val = nums[right]
            freq = count.get(val, 0)
            pairs += freq
            count[val] = freq + 1

            while pairs >= k:
                result += len(nums) - right

                leftVal = nums[left]
                count[leftVal] -= 1
                pairs -= count[leftVal]
                left += 1

        return result