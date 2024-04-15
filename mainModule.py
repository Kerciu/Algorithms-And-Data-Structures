from BSTTree import BSTTree
from AVLTree import AvlTree
import auxiliaryModule


def perform_operations_on_tree(array, tree, operation, step=1000, fill_already=False):
    time_table = []

    if fill_already:
        for i in range(step, len(array) + 1, step):
            subset_array = array[:i]
            perform_batch_operation(tree.insert, subset_array)

    for i in range(step, len(array) + 1, step):
        subset_array = array[:i]
        time = auxiliaryModule.process_algorithm_time(lambda: perform_batch_operation(operation, subset_array))
        time_table.append((i, time))

    return time_table


def perform_batch_operation(operation, subset_array):
    for num in subset_array:
        operation(num)


if __name__ == "__main__":
    BST_tree = BSTTree()
    AVL_tree = AvlTree()
    list_for_trees = auxiliaryModule.generate_list()
    table_bst_insert = perform_operations_on_tree(list_for_trees.copy(), BST_tree, BST_tree.insert)
    table_bst_delete = perform_operations_on_tree(list_for_trees.copy(), BST_tree, BST_tree.delete, fill_already=True)
    table_avl_insert = perform_operations_on_tree(list_for_trees.copy(), AVL_tree, AVL_tree.insert)
    table_bst_search = perform_operations_on_tree(list_for_trees.copy(), BST_tree, BST_tree.search, fill_already=True)
    table_avl_search = perform_operations_on_tree(list_for_trees.copy(), AVL_tree, AVL_tree.search, fill_already=True)

    auxiliaryModule.draw_computional_complexity([table_bst_insert, table_avl_insert], "BST and AVL trees insertion", plots=2)
    auxiliaryModule.draw_computional_complexity([table_bst_search, table_avl_search], "BST and AVL trees search", plots=2)
    auxiliaryModule.draw_computional_complexity(table_bst_delete, "BST tree deletion", plots=1)

    print("Computing times for each operation:\n")
    print("BST Insert\n")
    print(table_avl_insert)
    print("------------------------------------------\nAVL Insert\n")
    print(table_avl_search)
    print("------------------------------------------\nBST Delete\n")
    print(table_bst_delete)
    print("------------------------------------------\nBST Search\n")
    print(table_bst_insert)
    print("------------------------------------------\nAVL Search\n")
    print(table_bst_search)
    print("------------------------------------------\n")

    new_BST = BSTTree()
    new_AVL = AvlTree()
    perform_batch_operation(new_BST.insert, [i for i in range(1, 21)])
    perform_batch_operation(new_AVL.insert, [i for i in range(1, 21)])

    print("Graphical representation of BST Tree: \n")
    new_BST.print_tree()

    print("\nGraphical representation of AVL Tree: \n")
    new_AVL.print_tree()
