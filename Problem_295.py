from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.nums = SortedList()
        

    def addNum(self, num: int) -> None:
        # add the num to the list.
        self.nums.add(num)
        
        

    def findMedian(self) -> float:
        # if lenght is odd, return the middle.
        # else return average of the middle two.
        i = len(self.nums)//2
        if len(self.nums)%2 == 0:
            return ( self.nums[i] + self.nums[i-1] )/2
        else:
            return self.nums[i]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
