package main

import (
    "fmt"
)

/*528. Random Pick with Weight
https://leetcode.com/problems/random-pick-with-weight/description/

Given an array `w` of positive integers, where `w[i]` describes the weight of
index `i`, write a function `pickIndex` which randomly picks an index in
proportion to its weight.

Note:

  1. `1 <= w.length <= 10000`
  2. `1 <= w[i] <= 10^5`
  3. `pickIndex` will be called at most `10000` times.

**Example 1:**

    
    
    **Input:** ["Solution","pickIndex"]
    [[[1]],[]]
    **Output:** [null,0]
    

**Example 2:**

    
    
    **Input:** ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    [[[1,3]],[],[],[],[],[]]
    **Output:** [null,0,1,1,1,0]

**Explanation of Input Syntax:**

The input is two lists: the subroutines called and their arguments.
`Solution`'s constructor has one argument, the array `w`. `pickIndex` has no
arguments. Arguments are always wrapped with a list, even if there aren't any.


Similar Questions:
  Random Pick Index (random-pick-index)
  Random Pick with Blacklist (random-pick-with-blacklist)
  Random Point in Non-overlapping Rectangles (random-point-in-non-overlapping-rectangles)
*/
type Solution struct {
    
}


func Constructor(w []int) Solution {
    
}


func (this *Solution) PickIndex() int {
    
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(w);
 * param_1 := obj.PickIndex();
 */

func main() {
    fmt.Println()
}
