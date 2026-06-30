class Solution(object):
    def setZeroes(self, matrix):
        zero_rows = set()
        zero_columns = set()
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)
        for i in range(rows):
            for j in range(columns):
                if i in zero_rows or j in zero_columns:
                    matrix[i][j] = 0