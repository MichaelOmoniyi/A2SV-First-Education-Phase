class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     rotated = [0] * n

    #     for i in range(n):
    #         rotated[(i + k) % n] = nums[i]

    #     for j in range(n):
    #         nums[j] = rotated[j]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1

        reverse(0, n - 1) # reverse entire array
        reverse(0, k - 1) # reverse first k elements
        reverse(k, n - 1) # reverse n - k elements