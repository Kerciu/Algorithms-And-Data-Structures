from BSTTree import BSTTree
from AVLTree import AvlTree
import plot_functions


if __name__ == "__main__":
    n_values = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000, 30000]
    limit = 30000
    generated_list = plot_functions.generate_list(limit, limit)
    empty_bst_tree = BSTTree()
    empty_avl_tree = AvlTree()
    full_bst_tree = plot_functions.create_full_bst_tree(limit)
    full_avl_tree = plot_functions.create_full_avl_tree(limit)
    plot_functions.draw_plot(n_values, generated_list, "BST and AVL trees insertion", empty_bst_tree, empty_avl_tree, "insert")
    plot_functions.draw_plot(n_values, generated_list, "BST and AVL trees search", full_bst_tree, full_avl_tree, "search")
    plot_functions.draw_plot_deletion(n_values, generated_list, "BST tree deletion", full_bst_tree,)
    new_BST = plot_functions.create_full_bst_tree(15)
    new_AVL = plot_functions.create_full_avl_tree(15)
    print("Graphical representation of BST Tree: \n")
    new_BST.print_tree()
    print("\nGraphical representation of AVL Tree: \n")
    new_AVL.print_tree()
