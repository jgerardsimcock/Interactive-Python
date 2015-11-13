from bin_tree_class import *
from stack import *
import operator

# def buildParseTree(fpexp):
#   #listify the expression
#   fplist = fpexp.split()
#   pStack = Stack()
#   eTree = BinaryTree('')
#   currentTree = eTree

#   for i in fplist:
#     #implement the four rules we specified
#     if i == '(':
#       currentTree.insertLeft('')
#       pStack.push(currentTree)
#       #sets current tree to left child
#       currentTree = currentTree.getLeftChild()

#     #Case for where value is integer
#     elif i not in ['+', '-', '*', '/', ')']:
#         currentTree.setRootVal(int(i))
#         #identify the parent
#         parent = pStack.pop()
#         #move back up to the parent
#         currentTree = parent

#     #case when you have an operator
#     elif i in ['+', '-', '*', '/']:
#           currentTree.setRootVal(i)
#           currentTree.insertRight('')
#           pStack.push(currentTree)
#           currentTree = currentTree.getRightChild()

#     #Case when parentheses ends
#     elif i == ')':
#         currentTree = pStack.pop()

#     else:
#         raise ValueError

#   return eTree


# pt = buildParseTree("( ( 10 + 5 ) * 3 )")
# pt.postorder()



# from pythonds.basic.stack import Stack
# from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

#pt = buildParseTree("( ( 10 + 5 ) * 3 )")
#pt.postorder()  #defined and explained in the next section
#print pt

def evaluate(parseTree):
  opers = {'+': operator.add, '-':operator.sub, '*':operator.mul,
  '/':operator.truediv}

  #Check to see if left and right Children have values
  leftC = parseTree.getLeftChild()
  rightC = parseTree.getRightChild()

  #if values than we perform some operation
  if leftC and RightC:
      fn = opers[parseTree.getRootVal()]
      return fn(evaluate(leftC), evaluate(rightC))

  else: 
      return parseTree.getRootVal()


def preorder(tree):
  if tree:
      print(tree.getRootVal())
      preorder(tree.getLeftChild())
      preorder(tree.getRightChild())


def postorder(tree):
  if tree != None:
    postorder(tree.getLeftChild())
    postorder(tree.getRightChild())
    print(tree.getRootVal())

def postordereval(tree):
  opers = {'+': operator.add, '-':operator.sub, '*':operator.mul,
  '/':operator.truediv}

  res1 = None#values to compare
  res2 = None#values to compare

  if tree:
    res1 = postordereval(tree.getLeftChild())
    res2 = postordereval(tree.getRightChild())
    if res1 and res2:
      return opers[tree.getRootVal()](res1, res2)
    else:
      return tree.getRootVal()

def inorder(tree):
  if tree != None:
    inorder(tree.getLeftChild())
    print(tree.getRootVal())
    inorder(tree.getRightChild())


def printexp(tree):
  sVal = ''
  if tree:
    sVal = '(' + printexp(tree.getLeftChild())
    sVal = sVal + str(tree.getRootVal())
    sVal = sVal + printexp(tree.getRightChild())

  return sVal


