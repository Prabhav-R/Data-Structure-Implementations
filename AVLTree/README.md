# AVL TREE

" _an **AVL tree** (named after inventors **A**delson-**V**elsky and **L**andis) is a [self-balancing binary search tree](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree "Self-balancing binary search tree"). It was the first such [data structure](https://en.wikipedia.org/wiki/Data_structure "Data structure") to be invented.[[2]](https://en.wikipedia.org/wiki/AVL_tree#cite_note-2) In an AVL tree, the [heights](https://en.wikipedia.org/wiki/Tree_height "Tree height") of the two [child](https://en.wikipedia.org/wiki/Child_node "Child node") subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property. Lookup, insertion, and deletion all take [O](https://en.wikipedia.org/wiki/Big_O_notation "Big O notation")(log *n*) time in both the average and worst cases, where n is the number of nodes in the tree prior to the operation._ "

[source](https://en.wikipedia.org/wiki/AVL_tree) (Wikipedia)

## Methods Implemented

- get_height(node) [STATIC METHOD] -> returns height of the node
- \_get_height_diff(node) -> returns height difference between left and right subtree
- \_LLRotate(node) -> preform left rotation about node
- \_RRRotate(node) -> preform right rotation about node
- \_LRRotate(node) -> preform left right rotation about node
- \_RLRotate(node)-> preform right left rotation about node
- insert(node) -> insert node into AVL tree
- display() -> Pre-order display of AVL Tree
- search(val) -> searches AVL Tree for val, returns boolean value
- delete(node) -> deletes node from AVL Tree
