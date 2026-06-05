class Solution:
    def numOfDiffChars(self,word1:str,word2:str)->int:
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return diff

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord)!=len(endWord):
            return 0
        isEndWordInWordList=False
        
        wordList.append(beginWord)
        adj = defaultdict(list)
        
        for i in range(len(wordList)):
            if wordList[i] == endWord:
                isEndWordInWordList = True
            for j in range(i+1,len(wordList)):
                if len(wordList[i]) != len(wordList[j]):
                    return 0
                diff = 0
                for k in range(len(wordList[i])):
                    if wordList[i][k] != wordList[j][k]:
                        diff += 1
                        
                if diff == 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        if not isEndWordInWordList: 
            return 0
        visited = set()
        minpath, endFound = 1, False
        def bfs(w):
            nonlocal minpath, endFound
            q = deque()
            q.append(w)
            visited.add(w)
            while q:
                level = len(q)
                for i in range(level): # process 1 level at a time
                    cur = q.popleft()
                    
                    if len(adj[cur]) == 0:
                        continue
                    
                    for nei in adj[cur]:
                        if nei not in visited:
                            if nei == endWord:
                                endFound = True
                                minpath += 1
                                return
                            visited.add(nei)
                            q.append(nei)
                minpath += 1

        
        bfs(beginWord)
        if not endFound: 
            return 0
        return minpath