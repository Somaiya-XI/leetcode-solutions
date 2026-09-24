class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows =  defaultdict(list)
        cols =  defaultdict(list)
        squares =  defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[i])):
                v = board[i][j]
                if v == '.':
                    continue
                
                k = (i // 3, j // 3)
                if v in rows[i] or v in cols[j] or v in squares[k]:
                    return False
        
                rows[i].append(v)
                cols[j].append(v)
                squares[k].append(v)
        return True