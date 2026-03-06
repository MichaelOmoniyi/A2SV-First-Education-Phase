class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = len(nums1) - 1, n - 1

        while j > -1:
            if nums1[m - 1] > nums2[j] and m > 0:
                nums1[i] = nums1[m - 1]
                m -= 1
                i -= 1
            else:
                nums1[i] = nums2[j]
                j -= 1
                i -= 1