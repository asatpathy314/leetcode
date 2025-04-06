_end = "_end_"


class Trie:
    def __init__(self):
        self.tree = dict()

    def insert(self, word: str) -> None:
        level = self.tree
        for char in word:
            if level.get(char, False):
                level = level[char]
            else:
                level[char] = dict()
                level = level[char]
        level[_end] = _end

    def search(self, word: str) -> bool:
        level = self.tree
        for char in word:
            if not level.get(char, False):
                return False
            else:
                level = level[char]

        return level.get(_end, 0) == _end

    def startsWith(self, prefix: str) -> bool:
        level = self.tree
        for char in prefix:
            if not level.get(char, False):
                return False
            else:
                level = level[char]
        return True


"""
Basic implementation for a trie.
A trie is very simple, the idea is that we can track strings as prefixes. Many strings share
prefixes. Thus we can create a hashmap tree of string prefixes that we can traverse. We use
the _end dict element to indicate that for some inserted word the current letter is terminal. 
"""
