class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, key):
        if key < self.value:
            if not self.left:
                self.left = BSTNode(key)
            else:
                self.left.insert(key)
        elif key > self.value:
            if not self.right:
                self.right = BSTNode(key)
            else:
                self.right.insert(key)
        else:
            print("Key exists in the tree")

    def search(self, key):
        if key < self.value:
            if not self.left:
                return False
            else:
                return self.left.search(key)
        elif key > self.value:
            if not self.right:
                return False
            else:
                return self.right.search(key)
        else:
            return True

    def delete(self, key):
        if self is None:
            return None
        if key < self.value:
            self.left = self.left.delete(key)
        elif key > self.value:
            self.right = self.right.delete(key)
        else:
            if not (self.left or self.right):
                return None
            if not self.left and self.right:
                return self.right
            if not self.right and self.left:
                return self.left
            pointer = self.right
            while pointer.left:
                pointer = pointer.left
            self.value = pointer.value
            self.right = self.right.delete(self.value)
        return self

    def inorder_traversial(self):
        if self.left:
            self.left.inorder_traversial()
        print(self.value)
        if self.right:
            self.right.inorder_traversial()
