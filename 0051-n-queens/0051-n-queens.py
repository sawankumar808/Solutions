class Solution:
    def isSafe(self, rowindex, colindex, n, board):
        row=rowindex
        col=colindex
        #left horizontal
        while(col>=0):
            if board[row][col]=='Q':
                return False
            col-=1
        # left upper diagnol
        row=rowindex
        col=colindex
        while(row>=0 and col>=0):
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        #left lower diagnol
        row=rowindex
        col=colindex
        while(row<n and col>=0):
            if board[row][col]=='Q':
                return False
            row = row+1
            col = col-1
        return True


    def solve(self,board, n, colindex, ans ):
        if colindex>=n:
            temp = []
            for row in board:
                temp.append("".join(row))  # List of chars -> String
            ans.append(temp)
            return

        for rowindex in range(n):
            if self.isSafe(rowindex, colindex, n, board):
                board[rowindex][colindex]='Q'
                self.solve(board, n, colindex+1, ans)

                board[rowindex][colindex]="."

    def solveNQueens(self, n: int) -> list[list[str]]:
        
        board=[["."] * n for _ in range(n)]

        colindex=0
        ans=[]
        self.solve(board, n, colindex, ans)
        return ans
    

        