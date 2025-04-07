class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if digits == "":
            return []

        solns = []
        l = len(digits) - 1
        current = [""] * (l + 1)

        def dfs_rec(i):
            if i == l:
                for c in mapping[digits[i]]:
                    current[i] = c
                    solns.append("".join(current))
            else:
                for c in mapping[digits[i]]:
                    current[i] = c
                    dfs_rec(i + 1)

        dfs_rec(0)
        return solns


"""
This is the recursive soln, idea is we create a tree of possible letter combinations
and track the previous letters in current. Then we backtrack up the tree continously filling
in more and more possible combinations. Below is an iterative solution that also works
for this problem. It's similar but instead of constructing a DFS tree it's a sort of
BFS tree. 
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if digits == "":
            return []

        solns = mapping[digits[0]]

        for digit in digits[1:]:
            new_solns = []
            for soln in solns:
                for char in mapping[digit]:
                    new_solns.append(f"{soln}{char}")
            solns = new_solns

        return solns
