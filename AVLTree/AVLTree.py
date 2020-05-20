
class AVLNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1


class AVL:

    def __init__(self):
        self.root = None

    @staticmethod
    def get_height(node):
        if node == None:
            return 0
        return node.height

    def _get_height_diff(self, node):
        return self.get_height(node.left)-self.get_height(node.right)

    def _LLRotate(self, node):
        R = node.left
        node.left = R.right
        R.right = node

        node.height = 1+max(self.get_height(node.left),
                            self.get_height(node.right))

        R.height = 1+max(self.get_height(R.left),
                         self.get_height(R.right))

        return R

    def _RRRotate(self, node):

        R = node.right
        node.right = R.left
        R.left = node

        node.height = 1+max(self.get_height(node.left),
                            self.get_height(node.right))

        R.height = 1+max(self.get_height(R.left),
                         self.get_height(R.right))

        return R

    def _LRRotate(self, node):
        node.left = self._RRRotate(node.left)
        return self._LLRotate(node)

    def _RLRotate(self, node):
        node.right = self._LLRotate(node.right)
        return self._RRRotate(node)

    def _insert(self, node, val):
        if node == None:
            return AVLNode(val)

        if val <= node.data:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        node.height = 1+max(self.get_height(node.left),
                            self.get_height(node.right))

        balance_factor = self._get_height_diff(node)

        if balance_factor > 1 and val <= node.left.data:
            return self._LLRotate(node)

        if balance_factor > 1 and val > node.left.data:
            return self._LRRotate(node)

        if balance_factor < -1 and val > node.right.data:
            return self._RRRotate(node)

        if balance_factor < -1 and val <= node.right.data:
            return self._RLRotate(node)

        return node

    def insert(self, val):
        self.root = self._insert(self.root, val)
        return self.root

    def _display(self, node):
        if not node:
            return
        print(node.data)
        self._display(node.left)
        self._display(node.right)

    @staticmethod
    def getMinNode(node):
        if node == None or node.left == None:
            return node
        return node.getMinNode(node.left)

    # pre order display
    def display(self):
        return self._display(self.root)

    def _search(self, node, val):
        if node == None:
            return False
        return node.data == val or self._search(node.left, val) or self._search(node.right, val)

    def search(self, val):
        return self._search(self.root, val)

    def _delete(self, node, val):
        if node == None:
            return node

        if val < node.data:
            node.left = self._delete(node.left, val)
        elif val > node.data:
            node.right = self._delete(node.right, val)
        else:

            if node.left == None:
                temp = node.right
                node = None
                return temp

            if node.right == None:
                temp = node.left
                node = None
                return temp

            temp = self.getMinNode(node.right)

            node.data = temp.data

            node.right = self._delete(node.right, node.data)

        if node == None:
            return node

        node.height = 1+max(self.get_height(node.left),
                            self.get_height(node.right))

        balance_factor = self._get_height_diff(node)

        if balance_factor > 1 and val <= node.left.data:
            return self._LLRotate(node)

        if balance_factor > 1 and val > node.left.data:
            return self._LRRotate(node)

        if balance_factor < -1 and val > node.right.data:
            return self._RRRotate(node)

        if balance_factor < -1 and val <= node.right.data:
            return self._RLRotate(node)

        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)
        return self.root


def main():
    A = AVL()

    # A.insert(10)
    # A.insert(20)
    # A.insert(30)
    # A.insert(40)
    # A.insert(50)
    # A.insert(25)

    # A.display()

    # print(A.search(25))
    # A.delete(25)
    # print(A.search(25))

    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

    for num in nums:
        A.insert(num)

    A.display()

    print("***********************")

    A.delete(10)

    A.display()


if __name__ == "__main__":
    main()
