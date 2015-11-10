#from pythonds.basic.stack import Stack
class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    return self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) -1]

  def size(self):
    return len(self.items)



def stringList(string):
  list_front = []
  for char in string:
    list_front.append(char)
  return list_front

def listString(list_string):
  reverse_string = ""
  for i in range(len(list_string)):
    reverse_string = reverse_string + list_string.pop()
  print reverse_string

# list_string = stringList("apple")
#test
# listString(list_string)

def binary(a, l=[]):
  if a>0:
    l.append(a%2)
    return binary(a/2)
  else:
    return "".join(map(str,l[::-1]))

#test
#print binary(233)

def baseDivision(decNumber, base, l=[]):

    if decNumber > 0:
      l.append(decNumber%base)
      newDecNumber = decNumber/base  
      return baseDivision(newDecNumber, base)

    else:
      return "".join(map(str,l[::-1]))

#test
#print(baseDivision(25, 16))
#print(baseDivision(26, 26))

class Queue:
  def __init__(self):
    self.items = []#this initializes the data structure as a list

  def isEmpty(self):
    return self.items == []#evaluates to True or False

  def enqueue(self, item):
    return self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

#test
# q = Queue()
# l = ['item1', 'item2', '5', 'true']
# q.enqueue(l)

# print q.isEmpty()
# print q.size()

def hotPotato(namelist, num):
  """Simulate a queue, namelist is the index and num is a counter"""

  simqueue = Queue()
  for name in namelist:
    simqueue.enqueue(name)#Loads names into queue
  #print simqueue.size()
  while simqueue.size() > 1:
    #this loop will queue and dequeue names for 7 rounds
    for i in range(num):
      simqueue.enqueue(simqueue.dequeue())
  #then will start to pop values from the list until the list length is 1
    simqueue.dequeue()
  #
  return simqueue.dequeue()

#print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))





  



