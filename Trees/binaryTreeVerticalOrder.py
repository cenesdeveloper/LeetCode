# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Solution
        1 - Create a hashmap for keeping track of columns because bfs will already order them in level
        2 - keep track of min and max columns so we can return them without sorting we will just have to read them in order so each column will have its nodes from top to bottom
        3 - root is column 0 and as we go left we decrement by 1 and increment 1 for right
        """
        if root is None:
            return []

        cols = defaultdict(list)
        maxc, minc = 0, 0
        q = deque([(root, 0)])

        while q:
            node, col = q.popleft()
            cols[col].append(node.val)
            maxc = max(maxc, col)
            minc = min(minc, col)

            if node.left:         
                q.append((node.left, col-1))
            
            if node.right:
                q.append((node.right, col+1))
        
        return [cols[x] for x in range(minc, maxc + 1)]

