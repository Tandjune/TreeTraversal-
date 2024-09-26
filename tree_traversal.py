class Node:
    def __init__(self, value: int) -> None:
        self.value = value

    def set_value(self, new_value: int) -> None:
        self.value = new_value

class Tree:
    def __init__(self, root: Node, right:"Tree" = None, left:"Tree" = None) -> None:
        self.root = root
        self.right = right
        self.left = left

    def get_root(self) -> int:
        return self.root.value
    
    def set_left(self, left_tree: "Tree") -> "Tree":
        self.left = left_tree
        return self
        
    def set_right(self, right_tree: "Tree") -> "Tree":
        self.right = right_tree
        return self
    
    def df_search_tree(self, traversal: str = "inorder") -> str:
        left = ""
        right = ""
        if self.left:
            left = self.left.df_search_tree(traversal)
        if self.right:
            right = self.right.df_search_tree(traversal)
        if traversal == "inorder":
            return f"{left} {self.get_root()} {right}"
        if traversal == "preorder":
            return f"{self.get_root()} {left} {right}"
        if traversal == "postorder":
            return f"{left} {right} {self.get_root()}"