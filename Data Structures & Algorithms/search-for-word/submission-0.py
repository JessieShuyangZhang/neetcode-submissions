class Solution:
    def findChar(self,board: List[List[str]],char:str) -> List[List[int]]:
        res = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == char:
                    res.append([i, j])
        return res
    def exist(self, board: List[List[str]], word: str) -> bool:
        starts = self.findChar(board,word[0])

        def dfs(pos,charInd):
            if charInd == len(word)-1:
                return True
            i,j = pos[0], pos[1]
            nxtChInd = charInd+1
            board[i][j] = '#' # mark visited
            # up
            if i-1 >=0 and board[i-1][j] == word[nxtChInd]:
                if dfs([i-1,j],nxtChInd):
                    return True
            # down
            if i+1<len(board) and board[i+1][j] == word[nxtChInd]:
                if dfs([i+1,j],nxtChInd):
                    return True
            # left
            if j-1>=0 and board[i][j-1] == word[nxtChInd]:
                if dfs([i,j-1],nxtChInd):
                    return True
            # right
            if j+1<len(board[0]) and board[i][j+1] == word[nxtChInd]:
                if dfs([i,j+1],nxtChInd):
                    return True
            board[i][j] = word[charInd]
            return False
            
        for start in starts:
            if dfs(start, 0):
                return True
        return False
            