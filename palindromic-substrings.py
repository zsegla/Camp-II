# https://leetcode.com/problems/palindromic-substrings/



class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(2 * len(s) + 1):

            left = right = i // 2
            if i % 2 == 1:
                right += 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count
