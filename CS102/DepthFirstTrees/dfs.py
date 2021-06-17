import TreeNode

TreeNode.print_tree(TreeNode.sample_root_node)

# define a function that accept two parameters: root_node and target_value

def dfs(root, target, path=()):
    path += (root,)
    if root.value == target: # if root value is target, return root object
        return path 

    for child in root.children:
        node_found = dfs(child, target, path)

        if node_found is not None:
            return node_found
    return None

node = dfs(TreeNode.sample_root_node, "F")
print(node)
        