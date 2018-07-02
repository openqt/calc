package main

import (
    "fmt"
)

/*783. Minimum Distance Between BST Nodes
https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

Given a Binary Search Tree (BST) with the root node `root`, return the minimum
difference between the values of any two different nodes in the tree.

**Example :**

    
    
    **Input:** root = [4,2,6,1,3,null,null]
    **Output:** 1
    **Explanation:**
    Note that root is a TreeNode object, not an array.
    
    The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
    
              4
            /   \
          2      6
         / \    
        1   3  
    
    while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
    

**Note:**

  1. The size of the BST will be between 2 and `100`.
  2. The BST is always valid, each node's value is an integer, and each node's value is different.


Similar Questions:
  Binary Tree Inorder Traversal (binary-tree-inorder-traversal)
*/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDiffInBST(root *TreeNode) int {
    
}

func main() {
    fmt.Println()
}
