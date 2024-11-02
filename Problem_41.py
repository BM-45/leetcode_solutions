class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
       
        n = len(nums)
        
        # Step 1: Modify the array
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all numbers from 1 to n are present
        return n + 1





    """ 
    It's straight forward but took time O(nlogn)
    and another problem is i just mistook edgecases.
    but they asked for O(n).   
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Find the min and max, if min > 1 then it should be 1.

        nums.sort()
        k = 1
        for i in nums:
            if i > 0:
                if i <= k:
                    if i == k:
                        k += 1
                    else:
                        continue
                else:
                    return k
        
        return k
    """
                    


        
