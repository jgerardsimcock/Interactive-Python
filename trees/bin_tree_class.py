class BinaryTree:
  def __init__(self, rootObj):
    self.key = rootObj
    self.leftChild = None
    self.rightChild = None


  def insertLeft(self, newNode):
    if self.leftChild == None:
        self.leftChild = BinaryTree(newNode)

    else:
        t = BinaryTree(newNode)
        t.leftChild = self.leftChild #reset the current node to the child of the new node
        #insert current node as child of root node
        self.leftChild = t 

  def insertRight(self, newNode):
    if self.rightChild == None:
      self.rightChild = BinaryTree(newNode)

    else:
      t = BinaryTree(newNode)
      t.rightChild = self.rightChild
      self.rightChild = t


  def getRightChild(self):
    return self.rightChild

  def getLeftChild(self):
    return self.leftChild

  def setRootVal(self, newVal):
    self.key = newVal

  def getRootVal(self):
    return self.key

  def preorder(self):
    print self.key

    if self.leftChild:
      self.leftChild.preorder()

    if self.rightChild:
      self.rightChild.preorder()

  

