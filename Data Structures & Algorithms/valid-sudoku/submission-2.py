class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        for i in range(9):
            temp = {}
            for j in range(9):
                if board[i][j] >= "1" and board[i][j] <= "9":
                    if int(board[i][j]) not in temp:
                        temp[int(board[i][j])] = 1
                    else:
                        temp[int(board[i][j])] += 1
                    if temp[int(board[i][j])] > 1:
                        return False
        
        for i in range(9):
            temp = {}
            for j in range(9):
                if board[j][i] >= "1" and board[j][i] <= "9":
                    if int(board[j][i]) not in temp:
                        temp[int(board[j][i])] = 1
                    else:
                        temp[int(board[j][i])] += 1
                    if temp[int(board[j][i])] > 1:
                        return False

        temp1 = {}
        temp2 = {}
        temp3 = {}
        for i in range(9):
            if i % 3 == 0:
                temp1 = {}
                temp2 = {}
                temp3 = {}
            
            for j in range(9):
                if board[i][j] >= "1" and board[i][j] <= "9":
                    if j < 3:
                        if int(board[i][j]) not in temp1:
                            temp1[int(board[i][j])] = 1
                        else:
                            temp1[int(board[i][j])] += 1
                        if temp1[int(board[i][j])] > 1:
                            return False
                    if j >= 3 and j < 6:
                        if int(board[i][j]) not in temp2:
                            temp2[int(board[i][j])] = 1
                        else:
                            temp2[int(board[i][j])] += 1
                        if temp2[int(board[i][j])] > 1:
                            return False
                    if j >= 6:
                        if int(board[i][j]) not in temp3:
                            temp3[int(board[i][j])] = 1
                        else:
                            temp3[int(board[i][j])] += 1
                        if temp3[int(board[i][j])] > 1:
                            return False
        
        return True
                




            
        
        
