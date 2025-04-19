class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for s_char, t_char in zip(s, t):
            s_freq[s_char] += 1
            t_freq[t_char] += 1

        for key in s_freq:
            if s_freq[key] != t_freq[key]:
                return False

        return True
