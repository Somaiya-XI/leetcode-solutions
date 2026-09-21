class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns = defaultdict(set), defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                
                k = (i // 3, j // 3)

                if v in rows[i] or v in columns[j] or v in squares[k]:
                    return False
                
                rows[i].add(v)
                columns[j].add(v)
                squares[k].add(v)
        return True