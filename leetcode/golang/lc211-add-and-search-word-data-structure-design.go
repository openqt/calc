package main

import (
    "fmt"
)

/*211. Add and Search Word - Data structure design
https://leetcode.com/problems/add-and-search-word-data-structure-design/description/

Design a data structure that supports the following two operations:

    
    
    void addWord(word)
    bool search(word)
    

search(word) can search a literal word or a regular expression string
containing only letters `a-z` or `.`. A `.` means it can represent any one
letter.

**Example:**

    
    
    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true
    

**Note:**  
You may assume that all words are consist of lowercase letters `a-z`.


Similar Questions:
  Implement Trie (Prefix Tree) (implement-trie-prefix-tree)
  Prefix and Suffix Search (prefix-and-suffix-search)
*/
type WordDictionary struct {
    
}


/** Initialize your data structure here. */
func Constructor() WordDictionary {
    
}


/** Adds a word into the data structure. */
func (this *WordDictionary) AddWord(word string)  {
    
}


/** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
func (this *WordDictionary) Search(word string) bool {
    
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */

func main() {
    fmt.Println()
}
