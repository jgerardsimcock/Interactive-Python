def binarySearch(alist, item):

    first = 0
    last = len(alist - 1)
    found = False

    while first <= last and not found:
      midpoint = (first + last) // 2

      if alist[midpoint] == item:
        found = True

      else: 
        if item < alist[midpoint]: #compare values
          last = midpoint - 1 #reassign the last value with midpoint-1 as upper boundary

        else:
          first = midpoint + 1 #reassign first with midpoint + 1 as lower boundary


    return found


def binarySearchRecurse(alist, item):

  if len(alist) == 0:
    return False

  else: 
    midpoint = len(alist) // 2
    
    if alist[midpoint] == item:
      return True

    else: 

      if item < alist[midpoint]:
        return binarySearchRecurse(alist[:midpoint], item)

      else:
        return binarySearchRecurse(alist[midpoint+1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearchRecurse(testlist, 3))
print(binarySearchRecurse(testlist, 13))