# 78% testcases passed

class Solution:
    isSolutionExists = True
    errorMessage = ""

    @staticmethod
    def rebase_with_max(matrix, col):
        max = matrix[col][col]
        max_row = col

        for i in range(col + 1, n):
            if (abs(matrix[i][col]) > abs(max)):
                max = matrix[i][col]
                max_row = i

        matrix[col], matrix[max_row] = matrix[max_row], matrix[col]

    @staticmethod
    def is_infinite(matrix):
        for i in range(len(matrix)):
            if not matrix[i][i]:
                return True
        return False
    
    @staticmethod
    def is_incompatible(matrix):
        for i in range(len(matrix)):
            su = 0
            for j in range(len(matrix)):
                su += matrix[i][j]
            if (su == 0):
                return True
        return False

    @staticmethod
    def error():
        isSolutionExists = False
        errorMessage = "The system has no roots of equations or has an infinite set of them."

    @classmethod
    def solveByGauss(self, n, matrix):
        matrix_original = matrix
        res = [0 for i in range(n)]

        for j in range(n - 1):
            self.rebase_with_max(matrix, j)
    
            for i in range(j + 1, n):
                if (matrix[j][j] == 0):
                    self.error()
                    return res
                
                coeff = matrix[i][j] / matrix[j][j]
                matrix[i][-1] -= coeff * matrix[j][-1]
    
                for k in range(j, n):
                    matrix[i][k] -= coeff * matrix[j][k]
            
        if (self.is_infinite(matrix) or self.is_incompatible(matrix)):
            self.error()
            return res
        
        for i in range(n - 1, -1, -1):
            res[i] = (matrix[i][-1] - sum([matrix[i][j] * res[j] for j in range(i + 1, n)])) / matrix[i][i]
    
        for i in range(n):
            su = 0
            for j in range(n):
                su += matrix_original[i][j] * res[j]
    
            res.append(abs(matrix_original[i][-1] - su))

        return res
    
n = int(input())
m = []

for i in range(n):
    m.append(list(map(int, input().split())))


res = Solution.solveByGauss(n, m)
if (not Solution.isSolutionExists):
    print(Solution.errorMessage)
else:
    print(*res)

# # SimpleIterations.py
# 3
# 2 1 -1 8
# -3 -1 2 -11
# -2 1 2 -3

# Output:
# 2.0 3.0000000000000004 -0.9999999999999999 0.0 0.0 0.0


# SimpleIterations.py
# 3
# 1 1 1 6
# 0 2 5 -4
# 2 5 -1 27

# Output:
# 5.0 3.0 -2.0 0.0 0.0 0.0

# SimpleIterations.py
# 3
# 1 1 1 6
# 0 2 5 -4
# 2 5 -1 27

# Output:
# 5.0 3.0 -2.0 0.0 0.0 0.0