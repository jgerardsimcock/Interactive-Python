from stack import Stack

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum += i
    return theSum

#with recursion
def listsum_recurse(numList):
  #we get to a point where the length of the list is 1 and work up
  if len(numList) == 1:
      return numList[0]
  else:
      return numList[0] + listsum_recurse(numList[1:])


# print(listsum([1,3,5,7,9]))
# print(listsum_recurse([1,3,5,7,9]))


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
      return convertString[n]
    else: 
      return toStr(n//base, base) + convertString[n%base]



# print(toStr(1600,16))
# print(toStr(1200,16))

def stringReverse(s):
  #base case
  if len(s) <= 1:
    return s
  else:
    return stringReverse(s[1:]) +s[0]

print stringReverse("Stay Stoked")

recurseStack = Stack()

def toStrStack(n, base):
  convertString = "0123456789ABCDEF"
  while n > 0:
      if n < base:
          recurseStack.push(convertString[n])
      else: 
          recurseStack.push(convertString[n%base])

      n = n//base
  result = ""

  while not recurseStack.isEmpty():
    result += str(recurseStack.pop())
  return result

print(toStrStack(1453,16))



