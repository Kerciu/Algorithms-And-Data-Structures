class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def build_tree_from_heap(array):
        if not array:
            return None

        root = Node(array[0])
        nodes = [root]
        i = 0

        while i < len(array):
            node = nodes.pop(0)
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(array):
                node.left = Node(array[left_index])
                nodes.append(node.left)

            if right_index < len(array):
                node.right = Node(array[right_index])
                nodes.append(node.right)

            i += 1

        return root

    @staticmethod
    def print_heap(root, level=0):
        # Funkcja zwracająca korzeń kopca binarnego o strukturze:
        #        9
        #     10 7
        #   11
        #     9  8
        #        7

        if root is not None:
            Node.print_heap(root.right, level + 1)
            print("   " * level + str(root.value))
            Node.print_heap(root.left, level + 1)
