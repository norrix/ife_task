# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:24:07 2015

@author: norrix
"""

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word = False
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True
        

'''
trie = Trie()
trie.insert("somestring")
print(trie.search("key"))
print(trie.startsWith("some"))
'''