# coding=utf-8
import unittest

"""820. Short Encoding of Words
https://leetcode.com/problems/short-encoding-of-words/description/

Given a list of words, we may encode it by writing a reference string `S` and
a list of indexes `A`.

For example, if the list of words is `["time", "me", "bell"]`, we can write it
as `S = "time#bell#"` and `indexes = [0, 2, 5]`.

Then for each index, we will recover the word by reading from the reference
string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes
the given words?

**Example:**

    
    
    **Input:** words = ["time", "me", "bell"]
    **Output:** 10
    **Explanation:** S = "time#bell#" and indexes = [0, 2, 5].
    

**Note:**

  1. `1 <= words.length <= 2000.`
  2. `1 <= words[i].length <= 7.`
  3. Each word has only lowercase letters.


Similar Questions:

"""


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
