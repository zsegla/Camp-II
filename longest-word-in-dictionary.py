# https://leetcode.com/problems/longest-word-in-dictionary/



class Solution:
    def longestWord(self, words: List[str]) -> str:
        length_to_words = defaultdict(set)

        for word in words:      # map word lengths to set of words
            length_to_words[len(word)].add(word)

        candidates = {""}       # initial candidate is the empty string
        length = 0              # length of current candidates

        while True:

            next_candidates = set()

            for longer_word in length_to_words[length + 1]: # check if each longer word can be built from any candidate
                if longer_word[:-1] in candidates:
                    next_candidates.add(longer_word)

            if not next_candidates:
                return sorted(list(candidates))[0]          # sort to return lexicographically lowest

            length += 1
            candidates = next_candidates
