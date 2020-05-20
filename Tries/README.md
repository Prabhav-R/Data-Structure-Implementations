# TRIE

" _a **trie**, also called **digital tree** or **prefix tree**, is a kind of [search tree](https://en.wikipedia.org/wiki/Search_tree "Search tree")—an ordered [tree](<https://en.wikipedia.org/wiki/Tree_(data_structure)> "Tree (data structure)") [data structure](https://en.wikipedia.org/wiki/Data_structure "Data structure") used to store a [dynamic set](<https://en.wikipedia.org/wiki/Set_(abstract_data_type)> "Set (abstract data type)") or [associative array](https://en.wikipedia.org/wiki/Associative_array "Associative array") where the keys are usually [strings](<https://en.wikipedia.org/wiki/String_(computer_science)> "String (computer science)"). Unlike a [binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree "Binary search tree"), no node in the tree stores the key associated with that node; instead, its position in the tree defines the key with which it is associated; i.e., the value of the key is distributed across the structure. All the descendants of a node have a common [prefix](https://en.wikipedia.org/wiki/Prefix "Prefix") of the string associated with that node, and the root is associated with the [empty string](https://en.wikipedia.org/wiki/Empty_string "Empty string"). Keys tend to be associated with leaves, though some inner nodes may correspond to keys of interest. Hence, keys are not necessarily associated with every node._ "

[source](https://en.wikipedia.org/wiki/Trie)(Wikipedia)

## Methods Implemented

- insert(word) -> insert word into Trie
- display() -> Display all words in Trie
- search(word) -> searches Trie for word, returns boolean value
- delete(word) -> deletes word from Trie
- startsWith(str) -> checks if Trie contain words starting with str
- printAutoComplete(str) -> prints auto-complete suggestions for str
