## Connected Data Store

# Stage 1: Create a Connected Data Store : Create and implement a data structure similar to a blockchain based on the below requirements.

## Requirements:

### Data Store Object Structure:
- Each data store object should have:
  - Index: Unique identifier for the object.
  - Data: Maximum of 1024 bytes of characters.
  - Prev Hash: Hash of the previous data store object.
  - Current Hash: Hash generated based on cryptographic algorithm using Index, Data, and Prev Hash.

### Initial Block:
- The first block should have 0000 as the Prev Hash.

## Steps:
1. Define the data store object structure with the specified properties.
2. Implement a method to generate the hash of a data store object based on the cryptographic algorithm and input parameters.
3. Create the initial block with 0000 as the Prev Hash.

---

# Stage 2: Correction State

## Requirements:

### Correct Data Store Object:
- A data store object is considered correct if its hash follows a specified pattern (e.g., first 4 digits are zero).
- Addition of a Correction Value field in the object.

### Correction Value Calculation:
- The Correction Value should be calculated in such a way that when combined with other fields, it produces a hash with the specified pattern.

### Hash Update:
- Ability to find a particular object's Correction Value.
- Update the object's hash based on the new Correction Value.

### Recalculation Trigger:
- Updating any field in a data store object should trigger a recalculation of the hash.
- Recalculation should propagate to further connected data store objects.

## Steps:
1. Add a Correction Value field to the data store object.
2. Implement a method to calculate the Correction Value for an object to meet the specified hash pattern.
3. Update the hash of the object based on the new Correction Value.
4. Implement a function to find a particular object's Correction Value and update its hash.
5. Ensure that updating any field triggers hash recalculation and cascades to connected data store objects.


The solution can be created on any tech stack. 
Create a fork of this repository and build your solution on the fork and share the forked repository address over email in the stipulated time.
