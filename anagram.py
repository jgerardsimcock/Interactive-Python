"""We are going to look at a number of strategies to 
check to see if two words are anagrams"""

#method 1 is just checking off
#this is logically cumbersome to me
def anagramSolution1(s1,s2):
  alist = list(s2)

  pos1 = 0 
  stillOk = True

  while pos1 < len(s1) and stillOk:
    pos2 = 0
    found = False

    while pos2 < len(alist) and not found:
      if s1[pos1] == alist[pos2]:

        found = True

      else:

        pos2 += 1

    if found:
      alist[pos2] = None
    else:
      stillOk = False

    pos1 += 1

  return stillOk



#print anagramSolution1('abcd', 'dbcf')

#This runtime is going to be dependent on our sorting calls
#This will either be nlogn or n^2
def anagramSolution2(s1,s2):
  alist1 = list(s1)
  alist2 = list(s2)

  alist1.sort()
  alist2.sort()

  pos = 0
  matches = True

  while pos < len(s1) and matches:

    if alist1[pos] == alist2[pos]:
      pos += 1
    else:
      matches = False

  return matches


#print anagramSolution2('abfghl', 'tyuilp')


##Count and Compare
def anagramSolution4(s1,s2):
  #create two data structures that represent the 
  #number of times a particular index-value is observed
  c1 = [0]*26
  c2 = [0]*26

  for i in range(len(s1)):
    pos = ord(s1[i]) - ord('a')
    c1[pos] += 1

  for i in range(len(s2)):
    pos = ord(s2[i]) - ord('a')
    c2[pos] += 1


  #now iterate through the values of each created data structures
  j = 0
  stillOk = True

  while j < 26 and stillOk:
    if c1[j] == c2[j]:
      j += 1

    else: 
      stillOk = False

  return stillOk


print anagramSolution4('apple', 'paple')



