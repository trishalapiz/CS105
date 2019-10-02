"""
In this exercise you will modify this hash table class so that it uses double hashing for collision resolution. The hash table will also increase its size whenever its load factor is 0.75 or more. The hash table will contain key-data pairs. You can assume that keys will be integer values and data strings.

Task 5:implement a resize() function that increases the size of the hash table appropriately and rehashes all existing key-data pairs into the appropriate slots in the larger hash table. You will need to modify the put() function to use this resize() function appropriately.
"""
#Trisha Lapiz tlap632

class HashTable:
    def __init__(self):
        self.__size = 5
        self.__slots = [None] * self.__size
        self.__data = [None] * self.__size
        self.__deleted = "\0"
        self.__count = 0

    def hash_function(self, key, size):
        return key % size
    
    def rehash(self, old_hash, key, size): #alter to incorporate 2nd function
        skip_step = size - (key % (size-1) + 1)
        return (old_hash + skip_step) % size

    def get(self, key): #get item from hash value
        start_slot = self.hash_function(key,len(self.__slots))
        position = start_slot

        while self.__slots[position] != None: #while slots are occupied
            if self.__slots[position] == key:
                return self.__data[position]
            else:
                position = self.rehash(position, key, len(self.__slots))
                if position == start_slot: #back to beginning, didn't find the element
                    return None
        return None

    def put(self,key,data): #insert item in hash value
        hash_value = self.hash_function(key,len(self.__slots))
        if self.__slots[hash_value] == None or \
           self.__slots[hash_value] == self.__deleted: #if slot is empty
            self.__slots[hash_value] = key
            self.__data[hash_value] = data
            self.__count += 1 #increases when a new key-value pair is added
            if self.load() >= 0.75:
                self.resize()
        elif self.__slots[hash_value] == key: #if a key exists, just add value
            self.__data[hash_value] = data
        else: 
            next_slot = self.rehash(hash_value, key, len(self.__slots)) #finding the next empty slot
            while self.__slots[next_slot] != None\
                  and self.__slots[next_slot] != self.__deleted \
                  and self.__slots[next_slot] != key: #traversing to find empty slot
                next_slot = self.rehash(next_slot, key, len(self.__slots))
                if next_slot == hash_value: #if back to the start
                    return
            if self.__slots[next_slot] == None or \
               self.__slots[next_slot] == self.__deleted: #if slot is empty or there was a key-value pair that got deleted
                self.__slots[next_slot] = key
                self.__data[next_slot] = data
            else:
                self.__data[next_slot] = data
                
    def delete(self, key):
        start_slot = self.hash_function(key, len(self.__slots))
        position = start_slot
        key_in_slot = self.__slots[position]

        while key_in_slot != None: #if there is not an empty slot
            if key_in_slot == key:
                self.__slots[position] = self.__deleted
                self.__data[position] = self.__deleted
                self.__count -= 1 #decreases when a new key-value pair is added
                if self.load() >= 0.75:
                    self.resize()
                return None	
            else:
                position = self.rehash(position, key, len(self.__slots)) #traverse
                key_in_slot = self.__slots[position]
                if position == start_slot: #if back to the start
                    return None

    def __delitem__(self, key):
        return self.delete(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __getitem__(self,key):
        return self.get(key)

    def __len__(self):
        return self.__count

    def __contains__(self, key):
        return self.get(key) != None
    
    def load(self): #num of items in table divided by size, if big then more chance of collisions as table is filling up
        return self.__count/self.__size
    
    def resize(self): #The hash table will also increase its size whenever its load factor is 0.75 or more.
        new_slots = list(self.__slots)
        new_data = list(self.__data)
        
        prime_number = self.get_nearest_prime(self.__size)
        self.__slots += [None] * (prime_number - self.__size)
        self.__data += [None] * (prime_number - self.__size)
        self.__size = prime_number
        
        for index in range(len(new_data)):
            if new_data[index] != None:
                self[new_slots[index]] = new_data[index]
            
    def get_nearest_prime(self, n):
        if n > 1:
            for num in range(2*n, n+1, -1): 
                if num % 2 == 0: #check if even, it skips to next number in range
                    continue

                increment = 0 #inside so it resets

                #check for number of factors that is not 1
                for i in range(2, num+1): 
                    if num % i == 0:
                        increment += 1

                    if increment >= 2:
                        break #not a prime number

                #check if number is a prime number
                if increment == 1:
                    return num

    def __repr__(self):
        str_rep = "{"
        for i in range(len(self.__slots)):
            key = self.__slots[i]
            data = self.__data[i]
            info = ""
            if key == None or key == self.__deleted:
                info = ""
            else:
                if data == None:
                    info = str(key) + ":None"
                else:
                    info = str(key) + ":" + str(data)
            str_rep += info + ", "
        return str_rep[:-2] + "}"
