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
            return f" {self.get_root()} {left}{right}"
        if traversal == "postorder":
            return f"{left}{right} {self.get_root()} "
        
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
    

class BinarySearchTree (Tree):
    def addNode(self, value:int) -> "BinarySearchTree":
        node = Node(value)
        root = self.get_root()

        if root == value:
            return self
        if root > value:
            self.left = self.left.addNode(value) if self.left  else BinarySearchTree(node)
            return self
        if root < value:
            self.right = self.right.addNode(value) if self.right else BinarySearchTree(node)
            return self
    
    
    def set_left(self, left_tree: "BinarySearchTree") -> "BinarySearchTree":
        if self.get_root() > left_tree.get_root():
            self.left = left_tree
        return self
      
    def set_right(self, right_tree: "BinarySearchTree") -> "BinarySearchTree":
        if self.get_root() < right_tree.get_root():
            self.right = right_tree
        return self


node1 = Tree(Node(1))
node2 = Tree(Node(2))
node3 = Tree(Node(3))
node4 = Tree(Node(4))
node5 = Tree(Node(5))
node6 = Tree(Node(6))
node7 = Tree(Node(7))

r = node6.set_left(node5).set_right(node7)
l = node2.set_left(node1).set_right(node3)

tree = node4.set_left(l).set_right(r)

df1 = tree.df_search_tree()
df2 = tree.df_search_tree("preorder")
df3 = tree.df_search_tree("postorder")
bf = tree.bf_search_tree()
print(f"Inorder Depth-first search: {df1}")
print(f"Preorder Depth-first search: {df2}")
print(f"Postorder Depth-first search: {df3}")
print(f"Breadth-first search: {bf}")

node = BinarySearchTree(Node(3))
tree2 = node.addNode(1).addNode(2).addNode(0).addNode(5).addNode(4).addNode(6)

print("\nExamples for the binary search tree:\n")
df1 = tree2.df_search_tree()
df2 = tree2.df_search_tree("preorder")
df3 = tree2.df_search_tree("postorder")
bf = tree2.bf_search_tree()
print(f"Inorder Depth-first search: {df1}")
print(f"Preorder Depth-first search: {df2}")
print(f"Postorder Depth-first search: {df3}")
print(f"Breadth-first search: {bf}")