import timeit
import random
#Analysis of native python data structures and the runtime

#lists
#concatenate
def test1():
  l = []#create empty data structure to store result
  for i in range(1000): 
    l += [i]

#append
def test2():
  l = []
  for i in range(1000):
    l.append(i)

#list comprehension
def test3():
  l = [i for i in range(1000)]

def test4():
  l = list(range(1000))

def test5():
  return False


# t1 = timeit.Timer("test1()", "from __main__ import test1")
# print("concat", t1.timeit(number=1000), "milliseconds")

# t2= timeit.Timer("test2()", "from __main__ import test2")
# print("append", t2.timeit(number=1000), "milliseconds")

# t3 = timeit.Timer("test3()", "from __main__ import test3")
# print("listComp", t3.timeit(number=1000), "milliseconds")

# t4 = timeit.Timer("test4()", "from __main__ import test4")
# print("list range", t4.timeit(number=1000), "milliseconds")

# t5 = timeit.Timer("test5()", "from __main__ import test5")
# print("empty function", t5.timeit(number=1000), "milliseconds")

#Native Python functions

popzero = timeit.Timer("x.pop(0)", 
                        "from __main__ import x")

popend = timeit.Timer("x.pop()", 
                      "from __main__ import x")

# x = list(range(2000000))
# print popzero.timeit(number=1000)

# x = list(range(2000000))
# print popend.timeit(number=1000)

#We can see that as the n increases the run time of popzero rises linearly
#Whereas popend is constant time
# #print ("pop(0)", "pop()")
# for i in range(1000000, 10000001, 1000000):
#   x = list(range(i))
#   pt = popend.timeit(number=1000)
#   x = list(range(i))
#   pz = popzero.timeit(number=1000)
#   print(pz,pt)


#Let's look at Dictionaries and how they perform

#Running contains operation in dictionary vs. list
#Dictionary is constant time
#List is linear
for i in range(10000, 100001, 20000):
  t = timeit.Timer("random.randrange(%d) in x"%i,
                  "from __main__ import random, x")

  x = list(range(i))
  lst_time = t.timeit(number=1000)

  x = {j:None for j in range(i)}
  d_time = t.timeit(number=1000)

  print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))


