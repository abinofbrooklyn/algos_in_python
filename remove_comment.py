from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res, buffer, is_block = [], '', False

        for line in source:
            i = 0
            while i < len(line):
                if i < len(line)-1 and line[i] == '/' and line[i+1] =='/' and not is_block:
                    i = line[i]
                elif i < len(line)-1 and line[i] == '/' and line[i+1] =='*' and not is_block:
                    is_block = True
                    i += 1
                elif i < len(line)-1 and line[i] == '*' and line[i+1] =='/' and is_block:
                    is_block = False
                    i += 1
                elif not is_block:
                    buffer += line[i]
                i += 1

            if buffer and not is_block:
                res.append(buffer)
                buffer = ''

        return res

s = Solution()
s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
