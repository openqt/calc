# coding=utf-8
import unittest

"""916. Word Subsets
https://leetcode.com/problems/word-subsets/description/

We are given two arrays `A` and `B` of words.  Each word is a string of
lowercase letters.

Now, say that word `b` is a subset of word `a` ** ** if every letter in `b`
occurs in `a`, **including multiplicity**.   For example, `"wrr"` is a subset
of `"warrior"`, but is not a subset of `"world"`.

Now say a word `a` from `A` is _universal_ if for every `b` in `B`, `b` is a
subset of `a`.

Return a list of all universal words in `A`.  You can return the words in any
order.



**Example 1:**

    
    
    **Input:** A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
    **Output:** ["facebook","google","leetcode"]
    

**Example 2:**

    
    
    **Input:** A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
    **Output:** ["apple","google","leetcode"]
    

**Example 3:**

    
    
    **Input:** A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
    **Output:** ["facebook","google"]
    

**Example 4:**

    
    
    **Input:** A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
    **Output:** ["google","leetcode"]
    

**Example 5:**

    
    
    **Input:** A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
    **Output:** ["facebook","leetcode"]
    



**Note:**

  1. `1 <= A.length, B.length <= 10000`
  2. `1 <= A[i].length, B[i].length <= 10`
  3. `A[i]` and `B[i]` consist only of lowercase letters.
  4. All words in `A[i]` are unique: there isn't `i != j` with `A[i] == A[j]`.


Similar Questions:

"""


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
