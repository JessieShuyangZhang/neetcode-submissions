class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if cur.children[ord(word[i])-ord('a')] == None:
                node = TrieNode()
                cur.children[ord(word[i])-ord('a')] = node
            char = cur.children[ord(word[i])-ord('a')]
            if i == len(word)-1:
                char.endOfWord = True
            cur = char

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            node = cur.children[ord(word[i])-ord('a')]
            if not node:
                return False
            if i == len(word)-1 and (not node.endOfWord):
                return False
            cur = node
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            node = cur.children[ord(prefix[i])-ord('a')]
            if not node:
                return False
            cur = node
        return True
            
        