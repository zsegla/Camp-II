# https://leetcode.com/problems/number-of-matching-subsequences/



class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        letter_to_suffixes = defaultdict(list)  # map next char of a word to suffix after that char
        letter_to_suffixes["#"] = words         # special character will be matched initially
        result = 0

        for c in "#" + s:

            suffixes = letter_to_suffixes[c]    # cannot pop unless checking whether c is in letter_to_suffixes
            del letter_to_suffixes[c]

            for suffix in suffixes:

                if len(suffix) == 0:            # matched all of this word
                    result += 1
                    continue

                next_letter, next_suffix = suffix[0], suffix[1:]
                letter_to_suffixes[next_letter].append(next_suffix)

        return result
