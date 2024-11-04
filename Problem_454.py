
from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Combine the first two lists
        ab = Counter(a + b for a in nums1 for b in nums2)
        
        # Count the tuples
        return sum(ab[-c-d] for c in nums3 for d in nums4)
    
    """
    Stored the last one in a dictionary.
    and Iterated through 1st, 2nd and 3rd.
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        # Iterate through the 3 lists and check if their sum is in the fourth list.
        map = self.count_frequency_with_count(nums4)
        count = 0
        
        for i in nums1:
            for j in nums2:
                for k in nums3:
                    total = -(i + j + k)
                    if total in map:
                        count += map[total]
        
        return count
    
    def count_frequency_with_count(self, my_list):
        frequency = {}
        for item in set(my_list):
            frequency[item] = my_list.count(item)
        return frequency
    """

        
