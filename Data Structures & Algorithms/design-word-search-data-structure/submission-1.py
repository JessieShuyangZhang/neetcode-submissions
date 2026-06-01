class TrieNode: 
    def __init__(self):
        self.children = {} # char -> Optional[TrieNode]
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not cur.children.get(c,None): 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return False
        stack = []  # (node, index of word)
        c = word[0]
        if c == '.':
            for key, node in self.root.children.items():
                stack.append((node,0))
        else:
            if not self.root.children.get(c,None):
                return False
            stack.append((self.root.children[c],0))
        while stack:
            node, ind = stack.pop()
            if ind + 1 == len(word):
                return node.endOfWord
            c = word[ind+1]
            if c == '.':
                for _, child in node.children.items():
                    stack.append((child,ind+1))
            else:
                if not node.children.get(c,None):
                    continue
                stack.append((node.children[c],ind+1))
        return False
        
