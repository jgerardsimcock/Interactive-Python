import time
from random import randrange

def sumofN(n):
  
  theSum = 0 #set base value

  #iterate through sequence
  for i in range(1, n+1):
    #perform sum computation
    theSum += i #accumulator
    #return the value after all the computation is complete
  return theSum

#print (sumofN(3))


def sumofN2(n):

  start = time.time()

  theSum = 0
  for i in range(1, n+1):
    theSum  += i

    end =  time.time()

  return theSum, end-start


def sumofN3(n):
  start = time.time()

  value = (n*(n+1))/2

  end = time.time()

  return value, end-start


# #print sumofN3

# powers_of_ten = [100,1000,10000,100000,1000000]

# for n in powers_of_ten: 
#   print "Sum is %d required %10.9f seconds"%sumofN3(n)

#Run time on this is n*n or n^2
#We have to compare every value in the list to every other value

def findMinQuadratic(alist):
  #set a baseline
  overallmin = alist[0]
  #iterate through a list
  for i in alist:
    isoverallmin = True

    for j in alist:
      if i > j:
        isoverallmin = False

    if isoverallmin:
      overallmin = i

  return overallmin

#With only one loop, runtime is linear and we only compare 
#each value to the next value in the array
def findMinLinear(alist):

  min_so_far = alist[0]
  for i in alist:
    if i <= min_so_far:
      min_so_far = i

  return min_so_far


#Generate lists of 1000-10000 with values up to 100000
for listsize in range(1000,10001,1000):
  alist = [randrange(100000) for x in range(listsize)]

  start = time.time()

  print (findMinLinear(alist))

  end = time.time()

  print ("size: %d time: %f" % (listsize, end-start))



