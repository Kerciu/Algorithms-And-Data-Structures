from BSTTree import BSTTree
from AVLTree import AvlTree
import auxiliaryModule


def perform_operations_on_tree(array, tree, operation, step=1000, fill_already=False):
    time_table = []

    if fill_already:
        for i in range(step, len(array) + 1, step):
            subset_array = array[:i]
            insert_batch(tree, subset_array)

    for i in range(step, len(array) + 1, step):
        subset_array = array[:i]
        time = auxiliaryModule.process_algorithm_time(lambda: operation(tree, subset_array))
        time_table.append((i, time))

    return time_table


def insert_batch(tree, subset_array):
    for num in subset_array:
        tree.insert(num)


def delete_batch(tree, subset_array):
    for num in subset_array:
        tree.delete(num)


def search_batch(tree, subset_array):
    for num in subset_array:
        tree.search(num)


if __name__ == "__main__":
    BST_tree = BSTTree()
    AVL_tree = AvlTree()
    list_for_trees = auxiliaryModule.generate_list()
    table_bst_insert = perform_operations_on_tree(list_for_trees.copy(), BST_tree, insert_batch)
    table_bst_delete = perform_operations_on_tree(list_for_trees.copy(), BST_tree, delete_batch, fill_already=True)
    table_avl_insert = perform_operations_on_tree(list_for_trees.copy(), AVL_tree, insert_batch)
    table_bst_search = perform_operations_on_tree(list_for_trees.copy(), BST_tree, search_batch, fill_already=True)
    table_avl_search = perform_operations_on_tree(list_for_trees.copy(), AVL_tree, search_batch, fill_already=True)

    auxiliaryModule.draw_computional_complexity([table_bst_insert, table_avl_insert], "BST and AVL trees insertion", plots=2)
    auxiliaryModule.draw_computional_complexity([table_bst_search, table_avl_search], "BST and AVL trees search", plots=2)
    auxiliaryModule.draw_computional_complexity(table_bst_delete, "BST tree deletion", plots=1)
