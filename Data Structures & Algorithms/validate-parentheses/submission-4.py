class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets_map = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }

        for char in s:
            if char in brackets_map:
                if stack and stack[-1] == brackets_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return (len(stack) == 0)
            



        
        