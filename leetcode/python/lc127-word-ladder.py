# coding=utf-8
import unittest

"""127. Word Ladder
https://leetcode.com/problems/word-ladder/description/

Given two words ( _beginWord_ and _endWord_ ), and a dictionary's word list,
find the length of shortest transformation sequence from _beginWord_ to
_endWord_ , such that:

  1. Only one letter can be changed at a time.
  2. Each transformed word must exist in the word list. Note that _beginWord_ is _not_ a transformed word.

**Note:**

  * Return 0 if there is no such transformation sequence.
  * All words have the same length.
  * All words contain only lowercase alphabetic characters.
  * You may assume no duplicates in the word list.
  * You may assume _beginWord_ and _endWord_ are non-empty and are not the same.

**Example 1:**

    
    
    **Input:**
    beginWord =  "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    **Output:** 5
    
    **Explanation:** As one shortest transformation is  "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.
    

**Example 2:**

    
    
    **Input:**
    beginWord =  "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    
    **Output:**  0
    
    **Explanation:**  The endWord "cog" is not in wordList, therefore no possible ** ** transformation.


Similar Questions:
  Word Ladder II (word-ladder-ii)
  Minimum Genetic Mutation (minimum-genetic-mutation)
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()