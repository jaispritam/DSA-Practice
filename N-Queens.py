# leetcode
#51. N-Queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag1 = set()
        diag2 = set()
        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r - c) in diag1 or (r + c) in diag2:
                    continue

                board[r][c] = 'Q'
                col.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                backtrack(r + 1)

                board[r][c] = '.'
                col.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return res
