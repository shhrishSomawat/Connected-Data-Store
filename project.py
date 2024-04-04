import hashlib

class Data_Store_Object:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.correctionValue = 0
        self.current_hash = self.evaluate_hash()

    def evaluate_hash(self):
        return hash_function(self.index + self.data + self.previous_hash + str(self.correctionValue))

    def update_hash(self):
        self.current_hash = self.evaluate_hash()

def hash_function(data):
    return hashlib.sha256(data.encode()).hexdigest()

def calculate_correctionValue(data_store_object, pattern="0000"):
    while True:
        if data_store_object.evaluate_hash()[:len(pattern)] == pattern:
            break
        else:
            data_store_object.correctionValue += 1
            data_store_object.update_hash()

def update_hash_with_correctionValue(data_store_object):
    data_store_object.update_hash()

def update_data(data_store_object, index=None, data=None, previous_hash=None):
    if index:
        data_store_object.index = index
    if data:
        data_store_object.data = data
    if previous_hash:
        data_store_object.previous_hash = previous_hash
    data_store_object.update_hash()

# Create initial block
initial_block = DataStoreObject(0, "Genesis Block", "0000")
