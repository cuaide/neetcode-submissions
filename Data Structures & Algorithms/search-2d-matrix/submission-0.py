class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0]) 

        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][cols - 1]:
                l, r = 0, cols - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[i][mid] < target:
                        l = mid + 1
                    elif matrix[i][mid] > target:
                        r = mid - 1
                    else:
                        return True
        return False