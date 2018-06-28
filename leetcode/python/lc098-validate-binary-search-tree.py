# coding=utf-8
import unittest

"""98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/description/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

  * The left subtree of a node contains only nodes with keys **less than** the node 's key.
  * The right subtree of a node contains only nodes with keys **greater than** the node 's key.
  * Both the left and right subtrees must also be binary search trees.

**Example 1:**

    
    
    **Input:**
        2
       / \
      1   3
    **Output:** true
    

**Example 2:**

    
    
        5
       / \
      1   4
         / \
        3   6
    **Output:** false
    **Explanation:** The input is: [5,1,4,null,null,3,6]. The root node 's value
                 is 5 but its right child's value is 4.


Similar Questions:
  Binary Tree Inorder Traversal (binary-tree-inorder-traversal)
  Find Mode in Binary Search Tree (find-mode-in-binary-search-tree)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
