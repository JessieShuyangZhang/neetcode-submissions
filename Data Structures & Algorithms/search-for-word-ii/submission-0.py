class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self,word:str):
        cur = self.children
        for i in range(len(word)):
            if word[i] not in cur:
                cur[word[i]] = TrieNode()
            if i == len(word)-1:
                cur[word[i]].endOfWord = True
            cur = cur[word[i]].children

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trieroot = TrieNode()
        for word in words:
            trieroot.addWord(word)
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS,COLS=len(board),len(board[0])
        res,visited = set(),set()
        
        def dfs(r,c,node,wordSoFar):
            if (r<0 or c<0 or r>=ROWS or c>=COLS 
                or (r,c) in visited
                or board[r][c] not in node.children):
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            wordSoFar += board[r][c]
            if node.endOfWord:
                res.add(wordSoFar)
                
            for d0,d1 in dirs:
                dfs(r+d0,c+d1,node,wordSoFar)
            visited.remove((r,c))
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,trieroot,"")
        return list(res)