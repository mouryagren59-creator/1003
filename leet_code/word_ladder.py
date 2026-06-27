class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0
        queue = [(beginWord, 1)]
        while queue:
            word, steps = queue.pop(0)
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i + 1:]
                    if newWord in words:
                        queue.append((newWord, steps + 1))
                        words.remove(newWord)
        return 0
