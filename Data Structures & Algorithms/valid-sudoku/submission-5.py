class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows =  defaultdict(set)
        cols =  defaultdict(set)
        squares =  defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                v = board[i][j]
                if v == '.':
                    continue
                
                k = (i // 3, j // 3)
                if v in rows[i] or v in cols[j] or v in squares[k]:
                    return False
        
                rows[i].add(v)
                cols[j].add(v)
                squares[k].add(v)
        return True