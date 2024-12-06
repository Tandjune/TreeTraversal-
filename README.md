# **Binary Tree**

This code consists of an implementation of binary trees and binary search trees, which are a more specialised version of the previous one. Both also have the following methods:

- `df_search_tree` (Depth-first search): returns the path of nodes starting from the root node and first visits all nodes of one branch as deep as possible before backtracking. The different variants (inorder, preorder, postorder) are implemented.
- `bf_search_tree` (Breadth-first search):  returns the path of nodes starting from the root node and visits all the nodes at the current depth before moving on to the next depth in the tree.
- `depth`:  returns the depth of the tree.

The following methods are also available, but only for binary search trees:

- `addNode`: to add a node to the correct tree position.
- `search`: returns `true` if the element is in the tree and `false` otherwise.