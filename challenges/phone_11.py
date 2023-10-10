import re 

class Solution:
    def isValid(self, input):
        pattern = re.compile("^[0-9]{3}\.[0-9]+\.[0-9]{4}")
        return pattern.match(input) is not None
    
    
if __name__ == "__main__":
    s = Solution()
    input = "123.123.7890"
    print(s.isValid(input))