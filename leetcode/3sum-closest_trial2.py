class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[-1]
        n = len(nums)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if abs(currentSum - target) < abs(closestSum - target):
                    closestSum = currentSum
                    if closestSum == target:
                        break
                
                if currentSum > target:
                    right -= 1
                else:
                    left += 1
                

        return closestSum