class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.sum_matrix = [[0] * (self.cols + 1) for row in range(self.rows + 1)]

        for row in range(self.rows):
            prefix_sum = 0
            for col in range(self.cols):
                prefix_sum += matrix[row][col]
                above = self.sum_matrix[row][col + 1]
                self.sum_matrix[row + 1][col + 1] = prefix_sum + above


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # sum = 0
        # for row in range(row1, row2 + 1):
        #     for col in range(col1, col2 + 1):
        #         sum += self.matrix[row][col]
        # return sum
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottom_right = self.sum_matrix[row2][col2]
        above = self.sum_matrix[row1 - 1][col2]
        bottom_left = self.sum_matrix[row2][col1-1]
        top_left = self.sum_matrix[row1-1][col1-1]
        sum = bottom_right - above - bottom_left + top_left
        return sum

    

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)