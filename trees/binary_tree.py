def BinaryTree(r):
    return [r, [],[]]



def insertLeft(root, newBranch):
  #remove the value in the left branch and save it in var t
  t= root.pop(1)

  if len(t) > 1:
    #we insert the previous child as the left child 
    #of our new branch
    root.insert(1, [newBranch, t, []])
  #otherwise create a new branch with two empty child nodes
  else:
    root.insert(1, [newBranch, [], []])

  return root


def insertRight(root, newBranch):
  t = root.pop(2)

  if len(t) > 1:
    root.insert(2, [newBranch, t, []])

  else:
    root.insert(2, [newBranch, [], []])

  return root


#Access functions: getters and setters

def getRootVal(root):
  return root[0]


def setRootVal(root, newVal):
  root[0] = newVal

def getLeftChild(root):
  return root[1]

def getRightChild(root):
  return root[2]

