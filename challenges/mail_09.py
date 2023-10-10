import re

class Solution:
    def isValid(self, input):
        pattern = re.compile(r"^[a-zA-Z0-9.-_%+]+@[A-Za-z0-9]+\.[A-Za-z0-9]{2,9}$")
        return pattern.match(input) is not None
        

if __name__ == "__main__":
    s = Solution()
    input = "luciano@gmail.com"
    print(s.isValid(input))