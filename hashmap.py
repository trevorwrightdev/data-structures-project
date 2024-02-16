class HashMap:
 
    # Constructor
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
 
    # This function creates a list of empty lists, one for each bucket in the hash table.
    def create_buckets(self):
        return [[] for _ in range(self.size)]
 
    # This function takes a key and a value and inserts the key-value pair into the hash table.
    def insert(self, key, val):
       
        hashed_key = hash(key) % self.size
         
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            if record_key == key:
                found_key = True
                break
 
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
 
    # This function takes a key and returns the value associated with that key in the hash table.
    def get(self, key):
       
        hashed_key = hash(key) % self.size
         
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            if record_key == key:
                found_key = True
                break
 
        if found_key:
            return record_val
        else:
            return "No record found"

 