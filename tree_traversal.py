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