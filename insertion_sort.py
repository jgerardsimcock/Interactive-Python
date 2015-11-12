def insertionSort(alist):
  #the comparison starts at index 1 and compares backwards 
  #at increments of one
  #it evaluates and reassigns to its left
  #it indexes and increments from left to right
  for index in range(1, len(alist)):

    currentvalue = alist[index]
    position = index

    #Stays in this loop until these criteria are 
    #no longer true 
    while position > 0 and alist[position - 1] > currentvalue:
        alist[position] = alist[position - 1]
        position = position - 1

    #When above is not true it reassigns the current value
    alist[position] = currentvalue