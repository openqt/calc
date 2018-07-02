package main

import (
    "fmt"
)

/*648. Replace Words
https://leetcode.com/problems/replace-words/description/

In English, we have a concept called `root`, which can be followed by some
other words to form another longer word - let's call this word `successor`.
For example, the root `an`, followed by `other`, which can form another word
`another`.

Now, given a dictionary consisting of many roots and a sentence. You need to
replace all the `successor` in the sentence with the `root` forming it. If a
`successor` has many `roots` can form it, replace it with the root with the
shortest length.

You need to output the sentence after the replacement.

**Example 1:**  

    
    
    **Input:** dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    **Output:** "the cat was rat by the bat"
    

**Note:**  

  1. The input will only have lower-case letters.
  2. 1 <= dict words number <= 1000 
  3. 1 <= sentence words number <= 1000 
  4. 1 <= root length <= 100 
  5. 1 <= sentence words length <= 1000


Similar Questions:
  Implement Trie (Prefix Tree) (implement-trie-prefix-tree)
*/
func replaceWords(dict []string, sentence string) string {
    
}

func main() {
    fmt.Println()
}
