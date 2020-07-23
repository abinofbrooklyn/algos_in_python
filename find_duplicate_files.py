from typing import List

class Solution:
    def findDuplicates(self, paths: List[str]) -> List[List[str]]:
        dict = {}
        for path in paths:
            input = path.split(" ")
            prefix = input[0]
            for i in range(1, len(input)):
                file = input[i]
                two = file.split("(")
                key = two[1][0:len(two)-1]
                if key not in dict:
                    dict[key] = []
                dict[key].append(prefix + "/" + two[0])
        res = []
        for val in dict.values():
            if len(val) >= 2:
                res.append(val)
        return res

s = Solution()
print(s.findDuplicates(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
