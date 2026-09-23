class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isDuplicateRow(row: List[List[str]]):
            for i in range(9):
                hash_row = {}
                for j in range(9):
                    if board[i][j] not in hash_row or board[i][j] == ".":
                        hash_row[board[i][j]] = 1
                    else:
                        return False
            return True

        def isDuplicateColumn(column: List[List[str]]):
            for i in range(9):
                hash_column = {}
                for j in range(9):
                    if board[j][i] not in hash_column or board[j][i] == ".":
                        hash_column[board[j][i]] = 1
                    else:
                        return False
            return True

        def isSubBoxValid():
            for start_r in range(0, 9, 3):
                for start_c in range(0, 9, 3):
                    hash_box = {}
                    for i in range(3):
                        for j in range(3):
                            val = board[start_r + i][start_c + j]
                            if val == ".":
                                continue
                            if val in hash_box:
                                return False
                            hash_box[val] = 1
            return True
            
        return isDuplicateRow(board) and isDuplicateColumn(board) and isSubBoxValid()