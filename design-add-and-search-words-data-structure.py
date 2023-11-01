# https://leetcode.com/problems/design-add-and-search-words-data-structure/



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end_of_word

            char = word[idx]
            if char != '.':
                if char in node.children:
                    return dfs(node.children[char], idx + 1)
                else:
                    return False
            else:
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
                return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
