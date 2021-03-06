# coding=utf-8
import unittest

"""126. Word Ladder II
https://leetcode.com/problems/word-ladder-ii/description/

Given two words ( _beginWord_ and _endWord_ ), and a dictionary's word list,
find all shortest transformation sequence(s) from _beginWord_ to _endWord_ ,
such that:

  1. Only one letter can be changed at a time
  2. Each transformed word must exist in the word list. Note that _beginWord_ is _not_ a transformed word.

**Note:**

  * Return an empty list if there is no such transformation sequence.
  * All words have the same length.
  * All words contain only lowercase alphabetic characters.
  * You may assume no duplicates in the word list.
  * You may assume _beginWord_ and _endWord_ are non-empty and are not the same.

**Example 1:**

    
    
    **Input:**
    beginWord =  "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    **Output:**
    [
      [ "hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]
    

**Example 2:**

    
    
    **Input:**
    beginWord =  "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    
    **Output:** []
    
    **Explanation:**  The endWord "cog" is not in wordList, therefore no possible ** ** transformation.


Similar Questions:
  Word Ladder (word-ladder)
"""


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
