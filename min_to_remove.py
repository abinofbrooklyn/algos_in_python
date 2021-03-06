class Solution:
    def minToRemoveToMakeValid(self, s: str) -> str:
        def removeInvalid(string, open_symb, close_symb):
            balance = 0
            stack = []

            for char in string:
                if char == open_symb:
                    balance += 1
                if char == close_symb:
                    if balance == 0:
                        continue
                    balance -= 1
                stack.append(char)
            return "".join(stack)

        check_str = removeInvalid(s, "(", ")")
        string_in_reverse = removeInvalid(check_str[::-1], ")", "(")
        return string_in_reverse[::-1]

    def minToRemoveToMakeValid2(self, s: str) -> str:
        stack, res = [], [""] * len(s)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            if c == ")":
                if stack:
                    left = stack.pop
                    res[left] = s[left]
                    res[i] = c
            else:
                res[i] = c
        return ("").join(res)

s = Solution()
print(s.minToRemoveToMakeValid("lee(t(c)o)de)"))
print(s.minToRemoveToMakeValid("a)b(c)d"))
print(s.minToRemoveToMakeValid("))(("))
print(s.minToRemoveToMakeValid("(a(b(c)d)"))
