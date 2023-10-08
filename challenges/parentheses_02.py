class Solution:
    def isValid(self, word: str) -> bool:
        stack = []  # Use a stack to keep track of open parentheses

        mapping = {')': '(', '}': '{', ']': '['}  # Define a mapping of closing to opening parentheses

        for character in word:
            if character in mapping:  # If the character is a closing parenthesis
                top_element = stack.pop() if stack else '#'  # Pop the top element from the stack or use '#' if the stack is empty
                if mapping[character] != top_element:
                    return False
            else:
                stack.append(character)  # If it's an opening parenthesis, push it onto the stack

        return not stack  # If the stack is empty at the end, the string is valid

if __name__ == "__main__":
    string = input("")
    s = Solution()
    print(s.isValid(string))
