class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_prefix = 0

        # find shortest string
        min_len = float("inf")
        min_str = ""

        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
                min_str = s

        if min_str == "":
            return ""

        # find longest common prefix
        for i in range(min_len):
            for s in strs:
                if s[i] != min_str[i]:
                    return min_str[0:len_prefix]
            len_prefix += 1

        # if no missing letters return min string
        return min_str


"""
Vertical scanning solution in Python.

Another solution is sorting the array and comparing the first and last string
common prefix 
"""
