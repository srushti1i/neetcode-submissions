class WordDictionary:

    def __init__(self):
        self.root={}

    def addWord(self, word: str) -> None:
        cur=self.root
        for char in word:
            if char not in cur:
                cur[char]={}
            cur=cur[char]
        cur[True]=True

    def search(self, word: str) -> bool:
        def dfs(ind, node):
            cur=node
            for j in range(ind,len(word)):
                char=word[j]
                if char==".":
                    for child in cur:
                        if child is True:
                            continue
                        if dfs(j+1, cur[child]):
                            return True
                    return False
                else:
                    if char not in cur:
                        return False
                    cur=cur[char]
            return True in cur
        return dfs(0, self.root)
            
