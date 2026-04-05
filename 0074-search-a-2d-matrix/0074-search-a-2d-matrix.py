from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Convert 1D index to 2D index
            r = mid // cols
            c = mid % cols
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        