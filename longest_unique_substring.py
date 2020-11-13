class Solution:
    def longest_unique_character_substring(self, s: str) -> int:
        seen, start, cur_len, longest = {}, 0, 0, 0

        for i, letter in enumerate(s):
            if letter in seen and seen[letter] >= start:
                start = seen[letter] + 1
                cur_len = i - seen[letter]
                seen[letter] = i
            else:
                seen[letter] = i
                cur_len += 1

                if cur_len > longest:
                    longest = cur_len

        return longest

s = Solution()
print(s.longest_unique_character_substring("dsfdsfvssdfesxsqa"))
print(s.longest_unique_character_substring("abcdefghijklmnopqrstuvwxyz"))
print(s.longest_unique_character_substring("yxpqmadzzaeftazlkrnxqwy"))
