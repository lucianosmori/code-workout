import re

class Solution:
    def isValid(self, phone_number):
        pattern = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
        return pattern.match(phone_number) is not None


if __name__ == "__main__":
    #XXX-XXX-XXXX 
    s = Solution()
    num = "132-456-7890"
    print(s.isValid(num))