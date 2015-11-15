from graph import *

def knightGraph(boardsize):
  kntGraph = Graph()
  for row in range(boardsize):
    for col in range(boardsize):
       nodeId = postToNodeId(row, col, boardsize)
       newPositions = genLegalMoves(row, col,boardsize)

       for e in newPositions:
        nid = postToNodeId(e[0], e[1], boardsize)
        kntGraph.addEdge(nodeId,nid)

  return kntGraph



def postToNodeId(row, column, boardsize):
    return (row*boardsize) + column


def genLegalMoves(x,y, boardsize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]

    for i in moveOffsets:
      newX = x + i[0]
      newY = y + i[1]

      if legalCoord(newX, boardsize) and legalCoord(newY, boardsize):
          newMoves.append(newX,newY)

    return newMoves


def legalCoord(x, boardsize):
    if x>= 0 and x < boardsize:
        return True

    else:
        return False


def knightTour(n, path, u, limit):
  #u=current depth in tree
  #path = list of vertices visited up to this point
  #u =vertex in graph we wish to explore
  #limit = number of nodes in path

  u.setColor = ('gray')
  path.append(u)
  if n < limit:
    nbrList = list(u.getConnections())
    i = 0
    done = False
    while i < len(nbrList) and not done:

      if nbrList[i].getColor() == 'white':  

        done = knightTour(n+1, path, nbrList[i], limit)

      i += 1

    if not done: #backtrack
      path.pop()
      u.setColor('white')

  else:
    done = True

  return done

#Warnsdorff Algorithm
def orderbyAvail(n):
  resList = []

  for v in getConnections():
      if v.getColor() == 'white'
        c = 0
        for w in v.getConnections():
          if w.getColor() == 'white'
            c = c + 1

          resList.append((c,v))

  resList.sort(key=lambda x: x[0])
  return [y[1] for y in resList]