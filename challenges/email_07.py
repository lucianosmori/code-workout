import re

class Solution:
    def isValid(self, string):
        pattern = re.compile("^[a-zA-Z0-9]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$")
        return(pattern.match(string) is not None)


if __name__ == "__main__":
    input = "email@gmail.com"
    s = Solution()
    print(s.isValid(input))