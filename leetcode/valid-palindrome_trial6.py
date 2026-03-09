class Solution:
    def isPalindrome(self, s: str) -> bool:
        numericalDigits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        sStrOnly = ""
        
        for char in s.lower():
            if (ord(char) >= 97 and ord(char) <= 122) or (char in numericalDigits):
                sStrOnly += char
        print(sStrOnly)
        
        start, end = 0, len(sStrOnly) - 1

        while start < end:
            if sStrOnly[start] != sStrOnly[end]:
                return False
            start += 1
            end -= 1
        return True