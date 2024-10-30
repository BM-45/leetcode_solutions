class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return self.subarraysWithAtmostKDistinct(nums, k) - self.subarraysWithAtmostKDistinct(nums, k - 1)

    def subarraysWithAtmostKDistinct(self, nums, k):
        total = 0
        count_map = {}
        i = 0
        for j in range(len(nums)):
            if nums[j] not in count_map:
                count_map[nums[j]] = 0
            count_map[nums[j]] += 1
            
            while len(count_map) > k:
                count_map[nums[i]] -= 1
                if count_map[nums[i]] == 0:
                    del count_map[nums[i]]
                i += 1
            
            total += j - i + 1
        
        return total
