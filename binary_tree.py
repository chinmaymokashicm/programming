class Node:
    # Initialize a root node

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def print_tree(self):
        print(self.data)


