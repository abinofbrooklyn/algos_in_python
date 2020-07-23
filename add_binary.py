class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = ""
        i, j, carry = len(a)-1, len(b)-1, 0
        while i >= 0 or j >= 0 or carry:
            n = int(a[i]) if i >= 0 else 0
            m = int(b[j]) if j >= 0 else 0
            total += str((n + m + carry) % 2)
            carry = (n + m + carry) // 2
            i -= 1
            j -= 1
        return total[::-1]

s = Solution()
print(s.addBinary("10","1010"))
print(s.addBinary("11","101"))
print(s.addBinary("100","1111"))
print(s.addBinary("10001","1110"))
