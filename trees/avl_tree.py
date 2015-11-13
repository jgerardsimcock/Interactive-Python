from binary_search_tree import BinarySearchTree

class AVLTree(BinarySearchTree):

  def _put(self, key, val, currentNode):
    if key < currentNode.key:
      if currentNode.hasLeftChild():
        self._put(key, val, currentNode.LeftChild)
      else:
        current.LeftChild = TreeNode(key,val, parent = currentNode)

        self.updateBalance(currentNode.leftChild)
      
    else:
      if currentNode.hasRightChild():
          self._put(key,val, currentNode.rightChild)
      else:
        currentNode.rightChild = TreeNode(kel, val, parent = currentNode)

        self.updateBalance(currentNode.rightChild)

  def updateBalance(self,node):
    if node.balanceFactor > 1 or node.balanceFactor < -1:
        self.rebalance(node)
        return
    if node.parent != None:
      if node.isLeftChild():
              node.parent.balanceFactor += 1
      elif node.isRightChild():
              node.parent.balanceFactor -= 1

      if node.parent.balanceFactor != 0:
              self.updateBalance(node.parent)


  def rotateLeft(self, rotRoot):

    newRoot = rotRoot.rightChild
    rotRoot.rightChild = newRoot.leftChild
    if newRoot.leftChild != None:
      newRoot.leftChild.parent = rotRoot

    newRoot.parent = rotRoot.parent

    if rotRoot.isRoot():
        self.root = newRoot

    else:
        if rotRoot.isLeftChild():
             rotRoot.parent.leftChild = newRoot
        else:
          rotRoot.parent.rightChild = newRoot

    newRoot.leftChild = rotRoot
    newRoot.parent = newRoot

    rotRoot.balanceFactor = rotroot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)

    newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

  def rotateRight(self, rotRoot):

    newRoot = rotRoot.leftChild
    rotRoot.leftChild = newRoot.righChild

    if newRoot.rightChild != None:
       newRoot.rightChild.parent = rotRoot

    newRoot.parent= rotRoot.parent

    if rotRoot.isRoot():
      self.root = newRoot

    else:
      if rotRoot.isRightChild():
        rotRoot.parent.rightChild = newRoot

    newRoot.rightChild = rotRoot

    rotRoot.parent = newRoot

    rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
    newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)


  def rebalance(self, node):
    if node.balanceFactor < 0:
        if node.rightChild.balanceFactor > 0:
          self.rotateRight(node.rightChild)
          self.rotateLeft(node)
        else:
          self.rotateLef(node)

    elif node.balanceFactor > 0:
        if node.leftChild.balanceFactor < 0:
          self.rotateLeft(node.leftChild)
          self.rotateRight(node)
        else:
          self.rotateRight(node)








