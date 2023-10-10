import re

class Solution:
    def isValid(self, string):
        pattern = re.compile(r"^[a-zA-Z0-9.-_%+]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,9}$")
        return pattern.match(string )is not None


if __name__ == "__main__":
    s = Solution()
    string = "luciano@gmail.com"
    print(s.isValid(string))