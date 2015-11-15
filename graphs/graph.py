class Vertex:
  """Uses a dictionary to keep track of the 
  vertices to which it is connected and weight of edge."""
  def __init__(self, key):
    self.id = key
    self.connectedTo = {}

  def addNeighbor(self, nbr, weight=0):
    self.connectedTo[nbr] = weight

  def __str__(self):
      return str(self.id) + 'connectedTo:' + 
        str([x.id for x in self.connectedTo])

  def getConnection(self):
    return self.connectedTo.keys()

  def getId(self):
    return self.id

  def getWeight(self, nbr):
    return self.connectedTo[nbr]

    