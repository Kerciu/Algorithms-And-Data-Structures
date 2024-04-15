from BSTTree import BSTTree
from AVLTree import AvlTree
import auxiliaryModule


def insert_tree_elements(array, tree, step=1000):
    time_table = []

    for i in range(step, len(array) + 1, step):
        subset_array = array[:i]
        time = auxiliaryModule.process_algorithm_time(lambda: insert_batch(tree, subset_array))
        time_table.append((i, time))

    return time_table


def delete_tree_elements(array, tree, step=1000):
    time_table = []

    for i in range(step, len(array) + 1, step):
        subset_array = array[:i]
        insert_batch(tree, subset_array)

    for i in range(step, len(array) + 1, step):
        subset_array = array[:i]
        time = auxiliaryModule.process_algorithm_time(lambda: delete_batch(tree, subset_array))
        time_table.append((i, time))

    return time_table


def search_tree_elements(array, tree, step=1000):
    time_table = []

    for i in range(step, len(array) + 1, step):
        subset_array = array[:i]
        insert_batch(tree, subset_array)

    for i in range(step, len(array) + 1, step):
        subset_array = array[:i]
        time = auxiliaryModule.process_algorithm_time(lambda: search_batch(tree, subset_array))
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
    table_bst_insert = insert_tree_elements(list_for_trees.copy(), BST_tree)
    table_bst_delete = delete_tree_elements(list_for_trees.copy(), BST_tree)
    table_avl_insert = insert_tree_elements(list_for_trees.copy(), AVL_tree)
    table_bst_search = search_tree_elements(list_for_trees.copy(), BST_tree)
    table_avl_search = search_tree_elements(list_for_trees.copy(), AVL_tree)

    auxiliaryModule.draw_computional_complexity([table_bst_insert, table_avl_insert], "BST and AVL trees insertion", plots=2)
    auxiliaryModule.draw_computional_complexity([table_bst_search, table_avl_search], "BST and AVL trees search", plots=2)
    auxiliaryModule.draw_computional_complexity(table_bst_delete, "BST tree deletion", plots=1)
