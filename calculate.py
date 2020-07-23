class Solution:
    def calculate(self, s: str) -> int:
        s += "+0"
        stack, num, operation = [], 0, "+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == " ":
                continue
            else:
                if operation == "+":
                    stack.append(num)
                if operation == "-":
                    stack.append(-num)
                if operation == "*":
                    val = stack.pop()
                    stack.append((val * num))
                if operation == "/":
                    val = stack.pop()
                    stack.append(math.turc((val / num)))
                num, operation = 0, c
        return sum(stack)
