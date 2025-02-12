class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        r = s + t  
        res = ""   
        
        for char in r:
            if char in res:
                res = res.replace(char, "")  
            else:
                res += char  
        return res  
    
if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    
    solution = Solution()
    res = solution.findTheDifference(s, t)  
    print(res)  
