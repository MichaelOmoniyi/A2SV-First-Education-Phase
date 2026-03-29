class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        pre = 1
        post = 1
        product = [1] * len(nums)

        for i in range(1, len(nums)):
            pre *= nums[i-1]
            product[i] = pre

        for i in range(len(nums) - 2, -1, -1):
            post *= nums[i + 1]
            product[i] *= post

        return product