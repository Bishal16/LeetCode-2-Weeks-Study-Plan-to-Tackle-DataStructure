class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix), len(matrix[0])
        for i in range(r):
            if target>= matrix[i][0] and target<= matrix[i][c-1]:
                if target in matrix[i]:
                    return True
                else :
                    return False
        return False