import sys
sys.setrecursionlimit(int(1e9))

class Node:
    def __init__(self, data):
        self.num = data[0]
        self.data = data[1]
        self.level = data[2]
        self.left = None
        self.right = None
        

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while 1:
                if data[1] < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def preorder_traversal(self, node):
        if node is not None:
            result = []
            result.append(node.num)
            result += self.preorder_traversal(node.left)
            result += self.preorder_traversal(node.right)
            return result
        else:
            return []
        
    def postorder_traversal(self, node):
        if node is not None:
            result = []
            result += self.postorder_traversal(node.left)
            result += self.postorder_traversal(node.right)
            result.append(node.num)
            return result
        else:
            return []

def solution(nodeinfo):
    nodeinfo = [[idx + 1, x, y] for idx, (x, y) in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x:-x[2])
    tree = BinaryTree()
    for data in nodeinfo:
        tree.insert(data)
    
    answer = [tree.preorder_traversal(tree.root), tree.postorder_traversal(tree.root)]
    return answer

a = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(a))