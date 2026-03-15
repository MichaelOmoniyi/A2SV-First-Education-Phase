class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        if n % 2 == 1:
            return -1
        
        left, right, chemistrySum, res = 1, n - 2, skill[0] + skill[-1], skill[0] * skill[-1]
        
        while left < right:
            if (skill[left] + skill[right]) != chemistrySum:
                return -1
            res += skill[left] * skill[right]
            left += 1
            right -= 1
        return res