class Solution:
    def multiplyString(self, num1: str, num2: str) -> str:
        n1 = self.splitNum(num1)
        n2 = self.splitNum(num2)

        return str(sum([x*y for x in n1 for y in n2]))

    def splitNum(self, num):
        result = []
        power = len(num) - 1
        num = [int(digit) for digit in str(num)]

        for n in num:
            result.append(n*10**power)
            power -= 1
        return result

    def multiplyString2(self, num1: str, num2: str) -> str:
        def str_to_i(s):
            res = 0
            for c in s:
                res = res * 10 + ord(c) - ord('0')
            return res

        return str(str_to_i(num1) * str_to_i(num2))


s = Solution()
print(s.multiplyString("4342","4543"))
print(s.multiplyString("4545476863","4545476863"))
print(s.multiplyString("7273","3221"))
