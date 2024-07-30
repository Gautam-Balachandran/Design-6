# Space Complexity : O(t), where t is the total length of all sentences stored
# in the Trie
from collections import defaultdict, deque
import heapq

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.counts = defaultdict(int)
        self.is_word = False

class Pair:
    def __init__(self, s, c):
        self.s = s
        self.c = c

    def __lt__(self, other):
        if self.c == other.c:
            return self.s > other.s
        return self.c < other.c

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.prefix = ""
        for i in range(len(sentences)):
            self.add(sentences[i], times[i])
    
    # Time Complexity : O(n), where n is the length of the sentence
    def add(self, s, count):
        curr = self.root
        for c in s:
            curr = curr.children[c]
            curr.counts[s] += count
        curr.is_word = True

    # Time Complexity : O(p + m log m), where p is the length of the
    # prefix and m is the number of sentences with the given prefix
    def input(self, c):
        if c == '#':
            self.add(self.prefix, 1)
            self.prefix = ""
            return []
        
        self.prefix += c
        curr = self.root
        for char in self.prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        pq = []
        for s in curr.counts:
            heapq.heappush(pq, Pair(s, curr.counts[s]))

        res = []
        for _ in range(min(3, len(pq))):
            res.append(heapq.heappop(pq).s)
        return res

# Examples with time and space complexity analysis
if __name__ == "__main__":
    sentences = ["i love you", "island", "iroman", "i love leetcode"]
    times = [5, 3, 2, 2]
    ac = AutocompleteSystem(sentences, times)

    # Example 1
    print(ac.input('i')) # ["i love you", "island", "i love leetcode"]
    print(ac.input(' ')) # ["i love you", "i love leetcode"]
    print(ac.input('a')) # []
    print(ac.input('#')) # []

    # Example 2
    print(ac.input('i')) # ["i love you", "island", "i love leetcode"]
    print(ac.input(' ')) # ["i love you", "i love leetcode"]
    print(ac.input('a')) # []
    print(ac.input('#')) # []