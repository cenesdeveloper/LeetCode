class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Solution
        1 - run dfs from the O's that are at the edges and mark them T
        2 - convert all O's to X and all T's to O
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return

            board[r][c] = 'T'

            dfs(r+1, c)
            dfs(r, c+1) 
            dfs(r-1, c) 
            dfs(r, c-1)  
            return 
        
        # run dfs from top and bottom rows
        for i in range(cols):
            dfs(0, i)
            dfs(rows-1, i)
        
        # run dfs from first and last column
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        
        # Do the conversions

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
