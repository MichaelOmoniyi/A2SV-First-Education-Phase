class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1

        while left <= right:
            if left == right:
                return boats + 1

            weight = people[left] + people[right]
            boats += 1
            if weight > limit:
                right -= 1
            else:
                left += 1
                right -= 1
        return boats