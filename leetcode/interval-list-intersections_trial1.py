class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first, second = 0, 0
        closedIntervals = []
        
        while first < len(firstList) and second < len(secondList):
            if max(firstList[first][0], secondList[second][0]) <= min(firstList[first][1], secondList[second][1]):
                closedIntervals.append([max(firstList[first][0], secondList[second][0]), min(firstList[first][1], secondList[second][1])])
            
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1
        return closedIntervals