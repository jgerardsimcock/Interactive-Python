from deque import Deque


def palindromeChecker(aString):
    charDeque = Deque()

    for ch in aString:
      charDeque.addRear(ch)

    stillEqual = True
    while charDeque.size() > 1 and stillEqual:
      first = charDeque.removeFront()
      last = charDeque.removeRear()
      if first != last:
        stillEqual = False


    return stillEqual


print(palindromeChecker('radar'))
print(palindromeChecker("hannah"))

