class Solution(object):
    # There is a recursive formula here,
    # decode[k] = decode[k+1] + decode[K+2]
    # find the last two elements and fill the array.

    # Have to look at edge cases. 
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        decode = [0]*n

        # Last element.
        if 1 <= int(s[n-1]) <= 9 :
            decode[n-1] = 1
        # Last second element.
        if n >= 2:
            if 10 <= int(s[n-2:n]) <= 26:
                decode[n-2] = 1
            if 1 <= int(s[n-2]) <= 9:
                decode[n-2] += decode[n-1]
        i = n-3
        while i >= 0:
            if 1 <= int(s[i]) <= 9 :
                decode[i] = decode[i+1]
            if 10 <= int(s[i:i+2]) <= 26:
                decode[i] += decode[i+2]
            i-= 1

        return decode[0]
        
        
    # this function would return no of ways.
    # if string is empty would return 1 as it is leaf node
    # you add the value you get from the leaf node.
    """ Time limit exceeded for recursion
    def decode(self, string):
        if len(string) == 0:
            return 1
        if string[0] == '0':
            return 0
        
        if 1 <= int(string[0]) <= 9:
            result = self.decode(string[1:])
        if len(string) >= 2:
            if 10 <= int(string[:2]) <= 26:
                result += self.decode(string[2:])
                
        return result
    """
            
            
            
