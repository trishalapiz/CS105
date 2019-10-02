"""
Complete the buildTree function which takes the inorder and postorder traversal sequences of a tree as input arguments. The function then constructs the corresponding binary tree and returns it.
"""
def buildTree(inorder,preorder):  
    
    if len(preorder) == 0 and len(inorder) == 0:
        return None
    
    else:
        binary_tree = ListBinaryTree(preorder[0])
        """EXAMPLE: // INORDER = 0123456789 // PREORDER = 4321098765 """

        #GET THE ROOT VALUE OF BOTH SEQUENCES
        root_value = preorder[0] #4
        inorder_root_index = inorder.find(root_value) #4 is at index 4 FIND THE ROOT VALUE IN THE INORDER SEQUENCE

        #SPLIT THE INORDER SEQUENCE IN HALF TO GET SUBTREES
        inorder_left_subtree = inorder[:inorder_root_index] #[:4] so 0123
        inorder_right_subtree = inorder[inorder_root_index + 1:] #4+1 = 5 AND [5:] so 56789

        #SPLIT THE PREORDER SEQUENCE IN HALF TO GET SUBTREES
        preorder_left_subtree = preorder[1:inorder_root_index + 1] #3210
        preorder_right_subtree = preorder[inorder_root_index + 1:] #98765	    

        #CREATE TREE IN PREORDER TRAVERSAL // left tree, root value, right tree
        construct_tree = buildTree(inorder_left_subtree, preorder_left_subtree)
        binary_tree.insert_tree_left(construct_tree)
        construct_tree = buildTree(inorder_right_subtree, preorder_right_subtree)
        binary_tree.insert_tree_right(construct_tree)

    return binary_tree

tree = buildTree("42513","12453")
print(tree) #[1, [2, [4, None, None], [5, None, None]], [3, None, None]]

tree = buildTree("CS105","0SC15")
print(tree) #[0, [S, [C, None, None], [1, None, None]], [5, None, None]]
