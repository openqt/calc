# coding=utf-8
import unittest

"""110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the depth of the two subtrees of _every_ node never
differ by more than 1.

**Example 1:**

Given the following tree `[3,9,20,null,null,15,7]`:

    
    
        3
       / \
      9  20
        /  \
       15   7

Return true.  
  
**Example 2:**

Given the following tree `[1,2,2,3,3,null,null,4,4]`:

    
    
           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    

Return false.


Similar Questions:
  Maximum Depth of Binary Tree (maximum-depth-of-binary-tree)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
