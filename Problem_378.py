class Solution:

    # Novel idea in the range of smallest number to largest number.
    # We check no of elements less than the middle element.
    # We have interest range [left, right], now our goal is to find a mid
    # element where the no of elements to the right are equal to k-1. 
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]
        
        while left < right:
            mid = (left + right) // 2
            count = self.countLessOrEqual(matrix, mid)
            
            if count < k:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    def countLessOrEqual(self, matrix: List[List[int]], target: int) -> int:
        count = 0
        n = len(matrix)
        row, col = n - 1, 0
        
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1
        
        return count
