from queue import Queue


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
        
    def bf_search_tree(self) -> str:
        queue = Queue()
        res = ""
        adjascent_list = {}

        def get_chirdren(tree: Tree):
            if not tree:
                return adjascent_list
            
            r = tree.right.get_root() if tree.right else None
            l = tree.left.get_root() if tree.left else None
            adjascent_list[tree.get_root()] = [l, r]
            get_chirdren(tree.left)
            get_chirdren(tree.right)
            return adjascent_list
        
        get_chirdren(self)
        queue.put(self.get_root())

        while not queue.empty():
            item = queue.get()
            res += f"{item}  "
            for i in adjascent_list[item]:
                if i:
                    queue.put(i)
        return res