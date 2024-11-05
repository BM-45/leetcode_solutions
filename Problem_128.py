class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = self.sort_and_remove_duplicates(nums)
        count = 1
        current = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current += 1
            else:
                count = max(count, current)
                current = 1
        
        # Handle the case where the longest sequence is at the end
        count = max(count, current)
        
        return count
    
    def sort_and_remove_duplicates(self, arr):
        return sorted(set(arr))
