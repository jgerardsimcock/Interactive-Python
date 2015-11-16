def dijkstra(aGraph, start):
  """Shortest route when we know the structure of a graph"""

  pq = PriorityQueue()
  start - setDistance()
  pq.buildHeap([(v.getDistance(), v) for v in aGraph])

  while not pq.isEmpty():
    currentVert = pq.delMin()
    for nextVert in currentVert.getConnections():
        newDist = currentVert.getDistance() /
                  + currentVert.getWeight(nextVert)

        if newDist < nextVert.getDistance():
            nextVert.setDistance(newDist)
            nextVert.setPredecessor(currentVert)
            pq.decreaseKey(nextVert, newDist)

