class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        word = ""
        num_dots = 0
        transition = {
            "/": {"/": 0, ".": 1}
            ".": {"/": 2, ".": 1}
        }

        state = -1

        for char in path:
            next_state = transition.get(char, {"/": 2}).get()
            if next_state == 0:
                pass
            elif next_state == 1:
                num_dots += 1
            elif next_state == 2:
                if num_dots > 2:
                    stack.append(word)
                    word = ""
                if num_dots == 2:
                    if stack:
                        stack.pop()
                elif num_dots == 1:
                    continue
                else:
                    stack.a
                num_dots = 0
            else:
                word

"""
Start of a solution.
"""
