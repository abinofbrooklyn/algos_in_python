class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for token in path.split('/'):
            if token in ('','.'):
                continue
            elif token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)

    s = Solution()
    print(s.simplifyPath(""))
