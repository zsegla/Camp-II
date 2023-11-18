# https://leetcode.com/problems/longest-palindromic-subsequence/



class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if s == s[::-1]:    # early return for palindromes
            return n

        subsequence_2 = [0 for _ in range(n)]   # subsequences of length - 2 for each starting index
        subsequence_1 = [1 for _ in range(n)]   # subsequences of length - 1 for each starting index

        for length in range(2, n + 1):
            subsequence = []
            for i in range(0, n - length + 1):

                if s[i] == s[i + length - 1]:
                    subsequence.append(2 + subsequence_2[i + 1])
                else:
                    subsequence.append(max(subsequence_1[i], subsequence_1[i + 1]))

            subsequence_2 = subsequence_1
            subsequence_1 = subsequence

        return subsequence[0]
