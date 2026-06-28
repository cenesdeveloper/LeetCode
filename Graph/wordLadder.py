class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create Adjacency list
        pattern = defaultdict(list)
        wordList = [beginWord] + wordList

        for word in wordList:
            key = ""
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                pattern[key].append(word)
        
        # Run bfs
        res = 1
        seen = {beginWord}
        q = deque([beginWord])

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    p = word[:i] + "*" + word[i+1:]

                    for nei in pattern[p]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)

            res += 1
        return res if endWord in seen else 0
                