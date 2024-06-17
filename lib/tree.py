class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # Helper function for depth-first search
        def dfs(node):
            if node is None:
                return None
            
            # Check if the current node's id matches the desired id
            if node.get('id') == id:
                return node
            
            # Recursively search in the children
            for child in node.get('children', []):
                result = dfs(child)
                if result is not None:
                    return result
            
            return None

        # Start DFS from the root
        return dfs(self.root)
