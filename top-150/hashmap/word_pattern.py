class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match = [None for _ in range(26)]
        seen = set()
        s = s.split(" ")

        if len(s) != len(pattern):
            return False

        for c, word in zip(pattern, s):
            index = ord(c) - ord("a")
            if match[index] is not None:
                if word != match[index]:
                    return False
            else:
                if word in seen:
                    return False
                match[index] = word
                seen.add(word)

        return True
