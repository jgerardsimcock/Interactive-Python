from node import Node

class UnorderedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def isEmpty(self):
    return self.head == None
  #Each item of the list must reside in a Node object
  def add(self, item):
    temp = Node(item) #initialize the new Node with the item data
    temp.setNext(self.head) #we now need to link it into the structure of the list
    self.head = temp #reassign the value of head 

  def size(self):
    current = self.head#initialize current as the head
    count = 0
    while current != None: 
      count += 1
      current = current.getNext()#keep checking for the next value this will auto increment

    return count

  def search(self, item):
    current = self.head #start somewhere, initialize base
    found = False #initialize counter objects

    while current != None and not found:
        if current.getData() == item:
          found = True
        else:
          current = current.getNext()

    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False

    while not found:
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()

      if previous == None:
        self.head = current.getNext()
      else:
        previous.setNext(current.getNext())

  def append(self, item):
    current = self.head
    previous = None
    temp = Node(item)

    while current != None:
      previous = current
      current = current.getNext()

    previous.setNext(temp)




