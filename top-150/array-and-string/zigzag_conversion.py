class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        final_string = ""
        row = 0
        increment = (numRows - 1) + (numRows - 2) + 1
        i = 0
        odd_inc = True

        while len(final_string) != len(s):
            if i >= len(s):
                row += 1
                odd_inc = True
                i = row
            final_string += s[i]
            if row == 0 or row == numRows - 1:
                i = i + increment
            elif odd_inc:
                print(s[i], i, increment - row * 2)
                i = i + increment - row * 2
                odd_inc = False
            else:
                print(s[i], i, row * 2)
                i = i + row * 2
                odd_inc = True

        return final_string


"""
Confusing problem. Figured it out. Just a traversal pattern can determine manually. 
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        final = []
        switch = True

        for row in range(numRows):
            switch = True
            i = row
            while i < len(s):
                final.append(s[i])
                if row == 0 or row == numRows - 1:
                    i += 2 * (numRows - 1)
                else:
                    if switch:
                        i += 2 * (numRows - 1 - row)
                    else:
                        i += 2 * row
                    switch = not switch

        return "".join(final)


"""
A prettier solution with more efficient multiplication. 
"""
