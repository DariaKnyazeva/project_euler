    def insert(self, data, to_left=False):
        """
        This is to buils a binary tree, which is 
        """
        if self.data:
            if to_left:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data