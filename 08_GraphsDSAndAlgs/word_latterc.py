#!/usr/bin/env python3
import sys

from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        print(all_combo_dict)


        # Queue for BFS
        import collections
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()      
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
    start = "hit"
    end = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    s = Solution()
    print(s.ladderLength(start, end, words))

    start = "hit"
    end = "cog"
    words = ["hot","dot","dog","lot","log"]
    print(s.ladderLength(start, end, words))

    A = "drzugcvdxisdvbsvnpjt"
    B = "mqvuzbkqligdhppwkfsm"
    C =["xhgtqcmreskwhuauuepy", "domtiysdmnkdbmslupgt", "xfguqbmpesgwhonuufpy", "xfjuqbmpesgwhonuufpy", "qomtiysdmnkdbmslupgt", \
        "xojucbkpesgwhonuufpy", "xojucbkmlxgwhonwkfpy", "xhghqcmpesgwhcauufpy", "xojucbkpvsgwhonwufpy", "qhpthcmreskstmsfuegy", \
        "drzugcvdxisdvbsvntgt", "xhghqcwpesgwhcauufpy", "qoptiusdenkdnmsfuegy", "xhghqcmreslwhcauufpy", "xhghqcmresgwhcauufpy", \
        "qhpthcmresksxmsfuegy", "drzugyvdxisdvbsvntgt", "xfjucbkpesgwhonuufpy", "drzugcvdxisdvbsvnpgt", "xfgfqcwpesgwhfauufpy", \
        "qoptiysdtnkdnmsfuega", "ddmtgyvdmisdvbsvntgt", "qhgtqcmresksxmauuegy", "xojucbkpvxgwhonwufpy", "dgmtiyydmnkdbmsgupgc", \
        "xfgfqcwpesgwhcauufpy", "qomtiysdtnkdnmsfupga", "xqjuzbkmligdhoswkfsm", "domtiyydmnkdbmslupgt", "qhgtqcmreskwxmauuepy", \
        "ddmtiyvdmnsdvmsgntgt", "dgmtiyvdmnsdvmsgntgt", "xqjucbkmligwhonwkfpm", "qoptiusdenkdnmsfuega", "xqjuzbkmligwhoswkfpm", \
        "ddmtiyvdmisdvbsvntgt", "ddmtiyvdmnsdvbsgntgt", "qhpthcmresksxmauuegy", "ddmugyvdmisdvbsvntgt", "dgmtiyvdmnkdvmsgupgt", \
        "xfggqbwpesgwhfruufpy", "mqvuzbkqligdhopwkfsm", "qhpthumrenkdtmsfuegy", "qomtiysdtnkdnmslupgt", "dgmtiyvdmnkdvmsgntgt", \
        "qhgtqcmresksxmauuepy", "qopthumrenkdnmsfuegy", "xfluqbmpesgwhonuufpy", "qomtiysdtnkdnmsfupgl", "xfggqcwpesgwhfcuufpy", \
        "qhpthcmrekkstmsfuegy", "xhghqcmreskwhcauuepy", "xqauzbkqligdhopwkfsm", "dgmtiyvdmnkdbmsgupgc", "xfggqbwpesgwhfcuufpy", \
        "qoptiysdtnkdnmsfupga", "drzugcvdxisdvbsvnpjt", "xojucbkpvxgwhonwkfpy", "dgmtiyvdmnkdvmsgupgc", "qoptiusrenkdnmsfuegy", \
        "xhgfqcwpesgwhcauufpy", "dgmtiyydmnkdbmslupgc", "qopthumrenkdtmsfuegy", "qhpthcmresksxmsuuegy", "xhgtqcmreskwxuauuepy", \
        "drmugyvdxisdvbsvntgt", "drmugyvdmisdvbsvntgt", "dgmtiyydmnkdbmslupgt", "xfjuqbkpesgwhonuufpy", "mqvuzbkqligdhppwkfsm", \
        "mqauzbkqligdhopwkfsm", "xojucbkpvigwhonwufpy", "qomtiysdtnkdnmslupgl", "xojucbkpesgwhonnufpy", "qopthusrenkdnmsfuegy", \
        "xhghqcmreskwhcauufpy", "xojucbkpvsgwhonnufpy", "xqjuzbkqligdhopwkfsm", "dgmtiyvdmnkdvmsgutgt", "xojucbkplxgwhonwkfpy", \
        "qhpthcmrekkdtmsfuegy", "qoptiusdtnkdnmsfuega", "qhgthcmresksxmauuegy", "xhghqcmreskwhuauuepy", "xqjucbkmlxgwhonwkfpy", \
        "qomtiysdtnkdnmsfupgo", "xqjucbkmligwhoswkfpm", "xqjuzbkmligdhoswkfpm", "xfguqbwpesgwhonuufpy", "qhpthcmrenkdtmsfuegy", \
        "ddmtiyvdmisdvbsgntgt", "xfggqbwpesgwhonuufpy", "qomtiysdmnkdnmslupgt", "xhgtqcmreskwxmauuepy", "xqjuzbkqligdhoswkfsm", \
        "xfggqbwpesgwhoruufpy", "xfgfqcwpesgwhfcuufpy", "xqjucbkmligwhonwkfpy"]
    print(s.ladderLength(A, B, C))