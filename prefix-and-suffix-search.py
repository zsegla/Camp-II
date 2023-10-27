# https://leetcode.com/problems/prefix-and-suffix-search/



class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_root = [set(), [None for _ in range(26)]]   # trie node is set of words and list of next nodes
        self.suffix_root = [set(), [None for _ in range(26)]]   
        self.weights = {}                                       # map word to weight

        def insert(word, forwards):                             # insert a word into a trie
            if forwards:
                node = self.prefix_root
                iterate_word = word
            else:
                node = self.suffix_root
                iterate_word = word[::-1]

            node[0].add(word)
            for c in iterate_word:
                if not node[1][ord(c) - ord("a")]:              # create a new node of None
                    node[1][ord(c) - ord("a")] = [set(), [None for _ in range(26)]]
                node = node[1][ord(c) - ord("a")]
                node[0].add(word)

        for weight, word in enumerate(words):
            self.weights[word] = weight
            insert(word, True)
            insert(word, False)

    def f(self, prefix, suffix) -> int:

        def find_words(word, forwards):
            if forwards:
                node = self.prefix_root
                iterate_word = word
            else:
                node = self.suffix_root
                iterate_word = word[::-1]

            for c in iterate_word:
                node = node[1][ord(c) - ord("a")]
                if not node:
                    return -1       # early return if cannot match whole prefix or suffix
            return node[0]

        prefix_matches = find_words(prefix, True)
        suffix_matches = find_words(suffix, False)
        if prefix_matches == -1 or suffix_matches == -1:
            return -1

        matches = prefix_matches & suffix_matches
        weight = -1
        for match in matches:
            weight = max(weight, self.weights[match])
        return weight    

    
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
