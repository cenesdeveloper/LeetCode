class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Solution
        1 - different checks for rows, columns and 3x3 squares
        2 - for fast lookups hashmaps with set values for each
        """

        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True