# https://leetcode.com/problems/longest-common-subsequence/





class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        lcs = [0 for _ in range(n + 1)]

        for c1 in text1:            # for prefix of text1 up to and including c1
            new_lcs = [0]
            for j, c2 in enumerate(text2):  # for prefix of text2 up to and including c2
                if c1 == c2:
                    new_lcs.append(1 + lcs[j])
                else:
                    new_lcs.append(max(new_lcs[-1], lcs[j + 1]))
            lcs = new_lcs

        return lcs[-1]
