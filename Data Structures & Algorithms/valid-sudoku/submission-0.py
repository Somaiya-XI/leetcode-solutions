class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set),defaultdict(set), defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                v = board[i][j]

                if v == '.':
                    continue

                squareIndex = (i // 3, j // 3)
                if v in rows[i] or v in cols[j] or v in squares[squareIndex]:
                    return False

                rows[i].add(v)
                cols[j].add(v)
                squares[squareIndex].add(v)
        return True
        