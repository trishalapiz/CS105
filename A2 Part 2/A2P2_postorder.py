"""
Complete the postorder function which returns the postorder traversal sequence of an input tree.
"""

def buildTree(inorder,preorder):  
    
    if len(preorder) == 0 and len(inorder) == 0:
        return None
    
    else:
        binary_tree = ListBinaryTree(preorder[0])

        #GET THE ROOT VALUE OF BOTH SEQUENCES
        root_value = preorder[0] 
        inorder_root_index = inorder.find(root_value) 

        #SPLIT THE INORDER SEQUENCE IN HALF TO GET SUBTREES
        inorder_left_subtree = inorder[:inorder_root_index] 
        inorder_right_subtree = inorder[inorder_root_index + 1:]

        #SPLIT THE PREORDER SEQUENCE IN HALF TO GET SUBTREES
        preorder_left_subtree = preorder[1:inorder_root_index + 1] 
        preorder_right_subtree = preorder[inorder_root_index + 1:]

        #CREATE TREE 
        construct_left_tree = buildTree(inorder_left_subtree, preorder_left_subtree) #construct the left subtree
        binary_tree.insert_tree_left(construct_left_tree)
        construct_right_tree = buildTree(inorder_right_subtree, preorder_right_subtree) #construct the right subtree
        binary_tree.insert_tree_right(construct_right_tree)
        
        #print(binary_tree) doing this to see how tree is built

    return binary_tree
        
def postorder(tree): #tree -- pass tree object???
    a_string = ""  
    if (tree!=None):
        a_string = a_string + str(postorder(tree.get_left_subtree()))
        a_string = a_string +  str(postorder(tree.get_right_subtree()))
        a_string = a_string + tree.get_value()
    return a_string

#TEST CASES
tree = buildTree("42513","12453")
print(postorder(tree)) #45231

	
tree = buildTree("a*2+5/6-3","/+*a25-63")
print(postorder(tree)) #a2*5+63-/
