class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        def backtrack(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=len(board) or c>=len(board[0]) or board[r][c]!=word[i] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            res= (
                backtrack(r + 1, c, i + 1) or 
                backtrack(r - 1, c, i + 1) or 
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )
            visited.remove((r,c))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if backtrack(r,c,0):
                        return True
        return False
        