import hashlib

class DataStoreObject:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.data = data
        self.prev_hash = prev_hash
        self.correction_value = 0
        self.current_hash = self.calculate_hash()

    def calculate_hash(self):
        return hash_function(self.index + self.data + self.prev_hash + str(self.correction_value))

    def update_hash(self):
        self.current_hash = self.calculate_hash()

def hash_function(data):
    return hashlib.sha256(data.encode()).hexdigest()

def calculate_correction_value(data_store_object, pattern="0000"):
    while True:
        if data_store_object.calculate_hash()[:len(pattern)] == pattern:
            break
        else:
            data_store_object.correction_value += 1
            data_store_object.update_hash()

def update_hash_with_correction_value(data_store_object):
    data_store_object.update_hash()

def update_data(data_store_object, index=None, data=None, prev_hash=None):
    if index:
        data_store_object.index = index
    if data:
        data_store_object.data = data
    if prev_hash:
        data_store_object.prev_hash = prev_hash
    data_store_object.update_hash()

# Create initial block
initial_block = DataStoreObject(0, "Genesis Block", "0000")
