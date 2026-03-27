class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whiteCount = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                whiteCount += 1
        
        res = whiteCount
        
        # Sliding window
        for i in range(k, len(blocks)):
            # Add right
            if blocks[i] == 'W':
                whiteCount += 1
            
            # Remove left
            if blocks[i - k] == 'W':
                whiteCount -= 1
            
            res = min(res, whiteCount)
        
        return res