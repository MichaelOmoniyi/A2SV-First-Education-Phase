class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        from collections import defaultdict
        
        freq = defaultdict(int)
        left = 0
        res = 0
        
        for right in range(len(fruits)):
            freq[fruits[right]] += 1
            
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            
            res = max(res, right - left + 1)
        
        return res