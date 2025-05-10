class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)

        if len(s) == 0:
            return 0

        freq[s[0]] += 1

        l = 0
        r = 1
        max_len = 0

        while r < len(s):
            if freq[s[r]] < 1:
                freq[s[r]] += 1
            else:
                max_len = max(r - l, max_len)
                while s[l] != s[r]:
                    freq[s[l]] -= 1
                    l += 1
                l += 1
            r += 1
        return max(r - l, max_len)


"""
Create a sliding window where you maintain the count, moving the right pointer +1 each time and moving the left past the leftmost repeated character if the current rightmost chracter is repeated. 
"""
