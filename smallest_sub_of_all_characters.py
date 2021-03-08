class Solution():
    def get_shortest_unique_substring(self, arr: List[str], str: str) -> str:
        curr = {}
        unq = set(arr)
        left = right = 0
        output = ""
        output_length = float("inf")

        while right < len(str):
            curr[str[right]] = curr.get(str[right], 0) + 1
            while left < right and str[left] in curr and curr[str[left]] > 1:
                if str[left] not in unq:
                    left += 1
                    continue
                curr[str[left]] = curr.get(str[left], 0) - 1
                left += 1
            if len(curr) >= len(unq) and isValid(unq, curr.keys()):
                tmp = str[left:right+1]
                if len(tmp) < output_length:
                    output = tmp
                    output_length = len(tmp)
            right += 1
        return output

    def isValid(self, arr, keys):
        for c in arr:
            if c not in keys:
                return False
        return True
