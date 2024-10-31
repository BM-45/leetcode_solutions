class Solution:
    result1 = []
    def partition(self, s: str) -> List[List[str]]:
        # Use recursion, 
        # When you call string
        # result1 = []
        Solution.result1.clear()
        self.dfs(s, [])
        return Solution.result1
    
    def dfs(self, string, currentList):
        if len(string) == 0:
            Solution.result1.append(currentList[:])
            #return result
        
        for i, char in enumerate(string):
            if self.palindrome(string[0:i+1]):
                currentList.append(string[0:i+1])
                
                self.dfs(string[i+1:], currentList)
                
                currentList.pop()

        #return result
    
    def palindrome(self, s):
        # Compare the string with its reverse
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

# ** Note this point.
# In Python, when you append a list to another list, 
# you're actually appending a reference to that list,
# not a copy of its contents.
