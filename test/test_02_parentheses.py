from challenges.parentheses_02 import Solution

def test_02():
    s = Solution()
    assert s.isValid("[]") == True
    assert s.isValid("][") == False
    assert s.isValid("(]") == False    
    assert s.isValid("[]{}()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("][}{)(") == False
    assert s.isValid("{[]}") == True    
