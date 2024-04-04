# Connected Data Store

## Overview
This Python code implements a Connected Data Store, which is a data structure similar to a blockchain. It allows for the creation of data store objects with unique identifiers, data, and references to previous objects. The code also includes functionality for ensuring data integrity through hash validation and correction.

## Problem Statement
The goal of this project is to create a data structure that mimics the behavior of a blockchain, providing secure storage and verification of data. The system should be able to generate hashes for data store objects and ensure that the data remains intact and unaltered.

## Solution Approach
To achieve the objectives outlined in the problem statement, the following approach was taken:

1. **Data Store Object**: Defined a class `Data_Store_Object` to represent each object in the data store, containing attributes for index, data, previous hash, correction value, and current hash.

2. **Hash Generation**: Implemented a hash function using the hashlib library to generate hashes for data store objects based on their attributes.

3. **Correction Value Calculation**: Developed a function to calculate the correction value for a data store object, ensuring that the hash meets specified patterns (e.g., leading zeros).

4. **Hash Update**: Implemented methods to update the hash of a data store object after modifying its attributes or correction value.

## System Architecture
The system architecture consists of a Python script containing the implementation of the data store object and related functions. It follows an object-oriented design, with a clear separation of concerns between the data store object class and the hash generation/correction logic.

## Usage
To use the Connected Data Store, follow these steps:

1. Instantiate the initial block using the `DataStoreObject` class.
2. Modify data store objects as needed, updating their attributes and correction values.
3. Ensure data integrity by recalculating hashes and correction values when necessary.

## Documentation
### Data Store Object Class
#### Attributes
- `index`: Unique identifier for the object.
- `data`: Data stored in the object.
- `previous_hash`: Hash of the previous data store object.
- `correctionValue`: Correction value used for hash correction.
- `current_hash`: Hash generated based on cryptographic algorithm using index, data, previous hash, and correction value.

#### Methods
- `evaluate_hash()`: Method to calculate the hash of the data store object.
- `update_hash()`: Method to update the current hash of the object.

### Other Functions
- `hash_function(data)`: Function to generate a hash using the hashlib library.
- `calculate_correctionValue(data_store_object, pattern)`: Function to calculate the correction value for a data store object.
- `update_hash_with_correctionValue(data_store_object)`: Function to update the hash of a data store object with its correction value.
- `update_data(data_store_object, index, data, previous_hash)`: Function to update the attributes of a data store object and recalculate its hash.

## Contributors
-[Shrish Somawat]
