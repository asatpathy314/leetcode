class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in parentheses.keys():
                stack.append(char)
                continue
            if not stack:
                return False
            opening = stack.pop()
            if char != parentheses[opening]:
                return False
        return not bool(stack)


"""
Very simple solution. Parse each character adding it to the stack if its an "opening" character.
Otherwise pop the top of the stack and compare the current character to the popped to make sure they
correspond. Otherwise return false. Make sure the stack is empty at the end and has elements when
we pop otherwise return false. 
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif not stack or char != parentheses[stack.pop()]:
                return False
        return not bool(stack)


"""
Slightly simplified version.     
"""
