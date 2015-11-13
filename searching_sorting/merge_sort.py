def mergeSort(alist):
  print ("Splitting", alist)

  if len(alist) > 1:
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    #recursive calls to each side of list
    mergeSort(lefthalf)
    mergeSort(righthalf)

    i, j, k = 0, 0, 0

    while i < len(lefthalf) and j < len(righthalf):

      if lefthalf[i] < righthalf[j]:
        alist[k] = lefthalf[i]
        i +=1

      else:
        alist[k] = righthalf[j]
        j += 1
      #move the index of the list up once we
      #know the value for the new alist[k]
      k += 1

    #no more j values
    while i < len(lefthalf):
      alist[k] = lefthalf[i]
      i += 1
      k += 1
    #no more i values
    while j < len(righthalf):
      alist[k] = righthalf[j]
      j += 1
      k += 1

  print("Merging", alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)