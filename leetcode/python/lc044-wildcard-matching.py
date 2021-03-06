# coding=utf-8
import unittest

"""44. Wildcard Matching
https://leetcode.com/problems/wildcard-matching/description/

Given an input string (`s`) and a pattern (`p`), implement wildcard pattern
matching with support for `'?'` and `'*'`.

    
    
    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    

The matching should cover the **entire** input string (not partial).

**Note:**

  * `s` could be empty and contains only lowercase letters `a-z`.
  * `p` could be empty and contains only lowercase letters `a-z`, and characters like `?` or `*`.

**Example 1:**

    
    
    **Input:**
    s =  "aa"
    p = "a"
    **Output:** false
    **Explanation:**  "a" does not match the entire string "aa".
    

**Example 2:**

    
    
    **Input:**
    s =  "aa"
    p = "*"
    **Output:** true
    **Explanation:**  '*' matches any sequence.
    

**Example 3:**

    
    
    **Input:**
    s =  "cb"
    p = "?a"
    **Output:** false
    **Explanation:**  '?' matches 'c', but the second letter is 'a', which does not match 'b'.
    

**Example 4:**

    
    
    **Input:**
    s =  "adceb"
    p = "*a*b"
    **Output:** true
    **Explanation:**  The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
    

**Example 5:**

    
    
    **Input:**
    s =  "acdcb"
    p = "a*c?b"
    **Output:** false


Similar Questions:
  Regular Expression Matching (regular-expression-matching)
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
