class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for s_char in s:
            s_freq[s_char] += 1

        for t_char in t:
            t_freq[t_char] += 1
            if t_freq[t_char] > s_freq[t_char]:
                return False

        return True


"""
concept is very simple. at any point if the number of char in t > number of char in s
then it is impossible for t to be an anagram of s or vice versa. so we count freq in
s and then check the running account for more efficiency.
"""
