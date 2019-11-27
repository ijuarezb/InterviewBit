#!/usr/bin/env python3
import sys

# Shortest Unique Prefix
# https://www.interviewbit.com/problems/shortest-unique-prefix/
#
# Find shortest unique prefix to represent each word in the list.
#
# Example:
#
# Input: [zebra, dog, duck, dove]
# Output: {z, dog, du, dov}
# where we can see that
# zebra = z
# dog = dog
# duck = du
# dove = dov
#  NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TrieNode:
    def __init__(self):
        self.chars = {}
        self.count = 0

    def __getitem__(self, index):
        return self.chars[index]

    def __setitem__(self, index, item):
        self.chars[index] = item

    def __contains__(self, item):
        return item in self.chars

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __iadd__(self, word):
        tmp = self.root

        for char in word:
            if char not in tmp:
                tmp[char] = TrieNode()
            tmp = tmp[char]
            tmp.count += 1

        return self

    def uniquePrefix(self, word):
        tmp, i = self.root, 0
        for char in word:
            tmp = tmp[char]
            i += 1
            if tmp.count == 1:
                break
        return word[:i]

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        trie = Trie()
        for word in A:
            trie += word

        return [trie.uniquePrefix(word) for word in A]

    # @param A : list of strings
    # @return a list of strings
    def prefix_lightweight(self, l):
        out = []
        for i in range(len(l)):
            temp = l[:i] + l[i+1:]
            point = 0
            flag = True
            while flag:
                for k in temp:
                    if(l[i][:point+1] == k[:point+1]):
                        point += 1
                        flag = True
                        break
                    else:
                        flag = False
            out.append(l[i][:point+1])
        return(out)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()
    Input = ['zebra', 'dog', 'duck', 'dove']
    print(s.prefix(Input))

# class TreeNode(object):
#     def __init__(self):
#         self._children = {} # prefix to child
        
#     def add(self, prefix):
#         if prefix not in self._children:
#             self._children[prefix] = TreeNode()
#         return self._children[prefix]
#     def num(self):
#         return len(self._children)
#     def get(self, prefix):
#         # Assumes exists
#         return self._children[prefix]

# class PrefixTree(object):
#     def __init__(self, words):
#         self._root = TreeNode() # empty prefix for root
#         for word in words:
#             self.add(word)
    
#     def add(self, word):
#         node = self._root
#         for c in word:
#             node = node.add(c)
    
#     def get(self, word):
#         node = self._root
#         counts = []
#         for c in word:
#             counts.insert(0, node.num())
#             node = node.get(c)
#         # chop of uniques from the end
#         num_remove = 0
#         for count in counts:
#             if count != 1:
#                 break
#             num_remove += 1
#         return word[:-num_remove] if num_remove>0 else word
            
# class Solution:
#     # @param A : list of strings
#     # @return a list of strings
#     def prefix(self, A):
#         # build prefix tree
#         tree = PrefixTree(A)
#         # apply prefix tree
#         return [tree.get(a) for a in A]


