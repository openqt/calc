package main

import (
    "fmt"
)

/*480. Sliding Window Median
https://leetcode.com/problems/sliding-window-median/description/

Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

Examples:  

`[2,3,4]` , the median is `3`

`[2,3]`, the median is `(2 + 3) / 2 = 2.5`

Given an array _nums_ , there is a sliding window of size _k_ which is moving
from the very left of the array to the very right. You can only see the _k_
numbers in the window. Each time the sliding window moves right by one
position. Your job is to output the median array for each window in the
original array.

For example,  
Given _nums_ = `[1,3,-1,-3,5,3,6,7]`, and _k_ = 3.

    
    
    Window position                Median
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       1
     1 [3  -1  -3] 5  3  6  7       -1
     1  3 [-1  -3  5] 3  6  7       -1
     1  3  -1 [-3  5  3] 6  7       3
     1  3  -1  -3 [5  3  6] 7       5
     1  3  -1  -3  5 [3  6  7]      6
    

Therefore, return the median sliding window as `[1,-1,-1,3,5,6]`.

**Note:**  
You may assume `k` is always valid, ie: `k` is always smaller than input
array's size for non-empty array.


Similar Questions:
  Find Median from Data Stream (find-median-from-data-stream)
*/
func medianSlidingWindow(nums []int, k int) []float64 {
    
}

func main() {
    fmt.Println()
}