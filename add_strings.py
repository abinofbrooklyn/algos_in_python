class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j, carry = len(num1)-1, len(num2)-1, 0

        while i >= 0 or j >= 0:
            val1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            val2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            total = (val1 + val2 + carry ) % 10
            carry =  (val1 + val2 + carry ) // 10
            res.append(total)
            i -= 1
            j -= 1

        if carry:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])

s = Solution()
print(s.addStrings("0","0"))
print(s.addStrings("54","56"))
print(s.addStrings("5099","3430"))
print(s.addStrings("435","540"))
