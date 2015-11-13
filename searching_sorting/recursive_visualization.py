import turtle




def drawSpiral(myTurtle, lineLen):
  if lineLen > 0:
    myTurtle.forward(lineLen)
    myTurtle.right(10)
    drawSpiral(myTurtle,lineLen-5)


# drawSpiral(myTurtle,100)
# myWin.exitonclick()


def tree(branchLen, t):
  if branchLen > 5:
    t.forward(branchLen)
    t.right(20)
    tree(branchLen-15, t)
    t.left(40)
    tree(branchLen-15, t)
    t.right(20)
    t.backward(branchLen)


def drawTriangle(points, color, t):
  t.fillcolor(color)
  t.up()
  t.goto(points[0][0], points[0][1])
  t.down()
  t.begin_fill()
  t.goto(points[1][0], points[1][1])
  t.goto(points[2][0], points[2][1])
  t.goto(points[0][0], points[0][1])
  t.end_fill()


def getMid(p1,p2):
  return ( ( p1[0]+p2[0])/2, (p1[1] +p2[1])/2)


def sierpenski(points,degree, t):

    colormap = ['blue','red','green','white','yellow',
                'violet','orange']

    drawTriangle(points, colormap[degree], t)
    if degree > 0:
        sierpenski([points[0], 
                    getMid(points[0], points[1]),
                    getMid(points[0], points[1])],
                    degree-1, t)
        sierpenski([points[1], 
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                    degree-1, t)
        sierpenski([points[2], 
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                    degree-1, t)
def main():
  t = turtle.Turtle()
  myWin = turtle.Screen()
  myPoints = [[-100,-50],[0,100],[100,-50]]
  sierpenski(myPoints, 3, t)
  myWin.exitonclick()

main()