from priority_queue import *

def prim(G, start):

  pq = PriorityQueue()
  for v in G:
    #set distances to infinity
    v.setDistance(sys.maxsize)
    v.setPredecessor(None)
  start.setDistance(0)

  pq.buildHeap([(v.getDistance(), v) for v in G])

  while not pq.isEmpty():

    currentVert = pq.delMin()
    for nextVert in currentVert.getConnections():

      newCost = currentVert.getWeight(nextVert)

      if nextVert in pq and newCost < nextVert.getDistance():
          nextVert.setPredecessor(currentVert)
          nextVert.setDistance(newCost)
          pq.decreaseKey(nextVert, newCost)

