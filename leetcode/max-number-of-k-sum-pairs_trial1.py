class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numCount = {}
        maxOperation = 0

        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        print("Nums Dictionary Counter: ", numCount)

        for num in nums:
            complement = k - num
            print("Complement: ", complement)
            if complement in numCount:
                print("Complement in dictionary")
                if numCount[num] > 0:
                    numCount[num] -= 1
                    numCount[complement] -= 1
                    if numCount[num] >= 0 and numCount[complement] >= 0:
                        print("Operation found")
                        maxOperation += 1
                    print(maxOperation, numCount)
        return maxOperation