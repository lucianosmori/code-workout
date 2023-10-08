class Solution:
    def isValid(self, word: str) -> bool:
        open_parentheses = [ '(', '{', '['] 
        closed_parentheses= [ ')', '}', ']']
        
        try:
            for index, character in enumerate(word):
                if character in open_parentheses:
                    assert word[index + 1] == self.get_next_ascii(character)
                    continue
                elif character in closed_parentheses:
                    assert word[index - 1] == self.get_prior_ascii(character)
                    continue
                else:
                    return False
                                
            return True
        
        except Exception:
            return False

    def get_next_ascii(self, x):
        ascii = ord(x)
        next_char = chr(ascii + 2) if x != "(" else chr(ascii + 1)
        return next_char

    def get_prior_ascii(self, x):
        ascii = ord(x)
        prior_char = chr(ascii - 2) if x != ")" else chr(ascii - 1)
        return prior_char

if __name__ == "__main__":
    string = input("")
    s = Solution()
    print(s.isValid(string))