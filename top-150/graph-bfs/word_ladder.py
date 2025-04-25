class Solution:
    def ladderLength(self, begin_word, end_word, word_list):
        word_list = set(word_list)
        word_len = len(begin_word)

        if end_word not in word_list:
            return 0

        q = deque([(begin_word, 1)])

        while q:
            current, depth = q.pop()
            for pos in range(0, word_len):
                for char in range(97, 123):
                    potential_word = f"{current[0:pos]}{chr(char)}{current[pos + 1 :]}"
                    if potential_word in word_list:
                        if potential_word == end_word:
                            return depth + 1
                        word_list.remove(potential_word)
                        q.appendleft((potential_word, depth + 1))
        return 0


"""
BFS through the words keeping track of current depth and queue
and then at any point of we find a end_word in the path in the
list then return the current depth + 1. 
"""
