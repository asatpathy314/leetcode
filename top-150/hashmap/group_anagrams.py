class Solution:
    def groupAnagrams(self, strs: List[str]):
        anagrams = defaultdict(list)
        for s in strs:
            alphabet = [0 for _ in range(26)]
            for c in s:
                alphabet[ord(c) - ord("a")] += 1
            anagrams[tuple(alphabet)].append(s)
        return list(anagrams.values())


"""
It doesn't get simpler than this. Create a bucket of sorts for each possible frequency list and sort each
word into the correct bucket. Create buckets on demand. 
"""
