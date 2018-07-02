package main

import (
    "fmt"
)

/*330. Patching Array
https://leetcode.com/problems/patching-array/description/

Given a sorted positive integer array _nums_ and an integer _n_ , add/patch
elements to the array such that any number in range `[1, n]` inclusive can be
formed by the sum of some elements in the array. Return the minimum number of
patches required.

**Example 1:**

    
    
    **Input:** _nums_ = [1,3], _n_ = 6
    **Output:** 1 
    **Explanation:**
    Combinations of _nums_ are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
    Now if we add/patch 2 to _nums_ , the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
    Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
    So we only need 1 patch.

**Example 2:**

    
    
    **Input:** _nums_ = [1,5,10], _n_ = 20
    **Output:** 2
    **Explanation:** The two patches can be [2, 4].
    

**Example 3:**

    
    
    **Input:** _nums_ = [1,2,2], _n_ = 5
    **Output:** 0


Similar Questions:

*/
func minPatches(nums []int, n int) int {
    
}

func main() {
    fmt.Println()
}
