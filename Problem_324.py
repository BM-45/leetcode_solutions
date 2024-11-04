class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This is a relatively straight forward problem.
        # Sort the array, and re-arrange it.

        # Create a sorted copy of the input array
        arr = sorted(nums)
        n = len(nums)
        
        # Initialize two pointers
        # i points to the middle of the array (end of the smaller half)
        # j points to the end of the array
        i, j = (n - 1) >> 1, n - 1
        
        # Fill the original array in wiggle sort order
        for k in range(n):
            if k % 2 == 0:
                # Even indices get elements from the smaller half
                nums[k] = arr[i]
                i -= 1
            else:
                # Odd indices get elements from the larger half
                nums[k] = arr[j]
                j -= 1
        
        

        
