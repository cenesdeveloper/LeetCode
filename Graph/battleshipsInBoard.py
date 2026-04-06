class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        Solution
        1 - when you see X run dfs on it on 4 directions
        2 - count the number of connected Xs as 1 ship
        """
        rows, cols = len(board), len(board[0])

        ships = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] == '.':
                return
            
            board[r][c] = '.'
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    dfs(r, c)
                    ships += 1
        return ships
            