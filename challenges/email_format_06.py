import re

class Solution:
    def isValid(self, string):
        #pattern = re.compile("^[\dA-Z]@[\dA-Z].[\dA-Z]", re.IGNORECASE)
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$')
        return pattern.match(string) is not None

if __name__ == "__main__":
    s = Solution()
    word = "test@gmail.com"
    print(s.isValid(word))