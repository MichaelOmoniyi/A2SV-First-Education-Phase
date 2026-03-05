class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals so that overlapping intervals are together
        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            if stack[-1][1] >= intervals[i][0]: # Checks if the end of interval in the stack greater than the current start
                stack[-1] = [min(stack[-1][0], intervals[i][0]), max(stack[-1][1], intervals[i][1])]
            else:
                stack.append(intervals[i])
        return stack
        