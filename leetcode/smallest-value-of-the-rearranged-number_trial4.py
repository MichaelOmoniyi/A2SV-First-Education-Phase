class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            symbol = str(num)[0]
            nums = str(num)[1:]
            num = int(symbol + "".join(sorted(nums, reverse=True)))
        else:
            numList = list(map(int, str(num)))
            numList.sort()
            i = 0

            if numList[i] == 0:
                while numList[i] == 0 and i < len(numList) - 1:
                    i += 1

            numList[0], numList[i] = numList[i], numList[0]
            num = int("".join(map(str, numList)))
        return num