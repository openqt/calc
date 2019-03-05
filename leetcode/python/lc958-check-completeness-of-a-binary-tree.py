# coding=utf-8
import unittest

"""958. Check Completeness of a Binary Tree
https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/

Given a binary tree, determine if it is a _complete binary tree_.

_**Definition of a complete binary tree
from[Wikipedia](http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees):**_  
In a complete binary tree every level, except possibly the last, is completely
filled, and all nodes in the last level are as far left as possible. It can
have between 1 and 2 h nodes inclusive at the last level h.



**Example 1:**

**![](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-
tree-1.png)**

    
    
    **Input:** [1,2,3,4,5,6]
    **Output:** true
    **Explanation:** Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
    

**Example 2:**

**![](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-
tree-2.png)**

    
    
    **Input:** [1,2,3,4,5,null,7]
    **Output:** false
    **Explanation:** The node with value 7 isn't as far left as possible.
    



**Note:**

  1. The tree will have between 1 and 100 nodes.


Similar Questions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()