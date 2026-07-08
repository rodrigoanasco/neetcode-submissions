class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        #Check horizontal
        for i in range(len(board)):
            test = [0] * 9
            for j in range(len(board[i])):
                if('1' <= board[i][j] <= '9'):
                    position_in_array = int(board[i][j]) - 1
                    test[position_in_array] += 1
                    if(test[position_in_array] > 1):
                        return False
        
        #Check vertical
        for i in range(len(board)):
            test2 = [0] * 9
            for j in range(len(board[i])):
                if('1' <= board[j][i] <= '9'):
                    position_in_array = int(board[j][i]) - 1
                    test2[position_in_array] += 1
                    if(test2[position_in_array] > 1):
                        return False

        #Block
        group1 = [0] * 9
        group2 = [0] * 9
        group3 = [0] * 9
        count = 0
        for i in range(len(board)):
            if count == 3:
                count = 0
                group1 = [0] * 9
                group2 = [0] * 9
                group3 = [0] * 9
            for j in range(len(board[i]) - 6):
                if ('1' <= board[i][j] <= '9'):
                    position_in_array = int(board[i][j]) - 1
                    group1[position_in_array] += 1
                    if(group1[position_in_array] > 1):
                        return False
                if ('1' <= board[i][j + 3] <= '9'):
                    position_in_array = int(board[i][j + 3]) - 1
                    group2[position_in_array] += 1
                    if(group2[position_in_array] > 1):
                        return False
                if ('1' <= board[i][j + 6] <= '9'):
                    position_in_array = int(board[i][j + 6]) - 1
                    group3[position_in_array] += 1
                    if(group3[position_in_array] > 1):
                        return False
            count = count + 1
            print(group1, group2, group3)

        return True

