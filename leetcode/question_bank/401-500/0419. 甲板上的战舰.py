from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == "X" and (i == 0 or board[i-1][j] == ".") and (j == 0 or board[i][j-1] == "."):
                    ans += 1
        return ans