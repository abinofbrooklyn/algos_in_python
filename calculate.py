class Solution:
    def calculate(self, s: str) -> int:
        stack, num, operator = [], 0, "+"
        all_ops = {"+", "-", "*", "/"}
        nums = set(str(x) for x in range(10))

        for idx in range(len(s)):
            char = s[idx]

            if char in nums:
                num = num * 10 + int(char)

            if char in all_ops or idx == len(s)-1:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack[-1] *= num
                elif operator == "/":
                    stack[-1] = int(stack[-1] / num)
                num, operator = 0, char

        return sum(stack)
