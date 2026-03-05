class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        placeholder = 0
        seeker = 1
        count = 1

        while seeker < len(nums):
            if nums[seeker] > nums[placeholder]:
                placeholder += 1
                nums[placeholder] = nums[seeker]
                count += 1
            seeker += 1
        return count
        