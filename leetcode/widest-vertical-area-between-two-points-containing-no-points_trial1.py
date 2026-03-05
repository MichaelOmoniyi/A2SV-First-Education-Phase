class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        widestArea = 0

        for i in range(1, len(points)):
            widestArea = max(points[i][0] - points[i-1][0], widestArea)
        return widestArea