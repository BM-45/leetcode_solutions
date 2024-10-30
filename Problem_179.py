from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(i) for i in nums]
        nums = self.custom_sort(nums)
        
        result = "".join(nums)
        
        return "0" if result[0] == "0" else result
    
    @staticmethod
    def compare_strings(a, b):
        str_a, str_b = str(a), str(b)
        return int(str_b + str_a) - int(str_a + str_b)

    def custom_sort(self, nums):
        return sorted(nums, key=cmp_to_key(Solution.compare_strings))
#Points to be noted here is the logic of adding the strings in different order and checking.
# Here we can use different sort algorithms.
