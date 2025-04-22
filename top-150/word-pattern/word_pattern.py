from collections import defaultdict


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")

        if len(s) != len(pattern):
            return False

        word_to_letter = defaultdict(str)
        letter_to_word = defaultdict(str)

        for letter, word in zip(pattern, s):
            if not word_to_letter[word]:
                word_to_letter[word] = letter
            elif word_to_letter[word] != letter:
                return False
            if not letter_to_word[letter]:
                letter_to_word[letter] = word
            elif letter_to_word[letter] != word:
                return False

        return True


"""
Every word-to-letter mapping must be unique
along with every letter-to-word mapping wh-
ich is why I created two dictionaries for
this problem. 
"""
