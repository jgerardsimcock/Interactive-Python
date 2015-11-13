class HashTable:
  def __init__(self):
      self.size = 11 #Prime numbers are good for collision resolution algorithm efficiency
      self.slots =[None]*self.size
      self.data = [None]*self.size

  #We need to put values into hash table

  def put(self, key, data):
      #Create a hashvalue with the hashfunction
      hashvalue = self.hashfunction(key, len(self.slots))

      #check to see if there is an available slot
      #if the slot has not been initialized
      #assign the key/data pair to the values in parameters
      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      #If there is already a key assigned and it equals the current key/hashvalue
      #update the data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data
        #if there is different key for the same hashvalue 
        #we need to rehash
        else:
          nextslot = self.rehash(hashvalue, len(self.slots))
          
          #when we rehash, we need to rerun the logic above
          #1. Check to see if the slot has been initialized with a key
          #2. If so, check the key/hash combination if different 
            #set the key/data values to current key, data

          while self.slots[nextslot] != None and self.slots[nextslot] != key:

            nextslot = self.rehash(nextslot, len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot] = key
            self.data[nextslot] = data
          else:
            self.data[nextslot] = data

  def hashfunction(self, key, size):
      return key%size

  def rehash(self, oldhash, size):
      return (oldhash + 1)%size


#We need to retrieve values from the hash tables

  def get(self, key):
    startslot = self.hashfunction(key, len(self.slots))

    data = None
    stop = False
    found = False
    position = startslot

    while self.slots[position] != None and not stop and not found:

        if self.slots[position] == key:
          found = True
          data = self.data[position]
        else:
          position = self.rehash(position, len(self.slots))

          if position == startslot:
            stop = True

    return data

  def __getitem__(self,key):
    return self.get(key)

  def __setitem__(self, key, data):
      self.put(key,data)

H = HashTable()

H[54] = "surf"
H[26]="Stay stoked"
H[93]="Bali"
H[17]="Ericeira"
H[77]="Rio"
H[31]="Keramas"
H[44]="Gas Chambers"
H[55]="Sunset"
H[20]="Ala Moana"

H.slots