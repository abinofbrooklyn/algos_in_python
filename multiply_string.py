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

s = Solution()
print(s.multiplyString("4342","4543"))
print(s.multiplyString("4545476863","4545476863"))
print(s.multiplyString("7273","3221"))
