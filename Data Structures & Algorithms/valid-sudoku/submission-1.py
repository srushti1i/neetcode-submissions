class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=[set() for _ in range(9)]
        c=[set() for _ in range(9)]
        d=[set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                val=board[row][col]
                if val== ".":
                    continue
                p=(row//3)*3+(col//3)

                if val in r[row] or val in c[col] or val in d[p]:
                    return False
                r[row].add(val)
                c[col].add(val)
                d[p].add(val)
        
        return True
