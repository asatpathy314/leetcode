class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = []
        prev = None

        for i, char in enumerate(s):
            if char == " ":
                if prev is not None:
                    words.append(s[prev:i])
                    prev = None
            elif prev is None:
                prev = i

        if prev is not None:
            words.append(s[prev:])

        return " ".join(words[::-1])


"""
Beats 100%. It's a very simple solution that probably makes more intuitive
sense than the one-liner below. Strip the text, then iterate through the
string character by character. Keep track of the beginning of each word and once you
encounter a space add the word to the list and set prev_char to None. Then once you encounter
a word again set prev to the first character of that word. Pretty chill. 
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


"""
Pretty chill one-liner. 
"""
