## Connected Data Store

## Requirement :
Create a data store similar to a blockchain to create a connected chain of nodes storing data which are verifiable and tamper proof.

### Stage 1: Create a Connected Data Store

- The  Data Store Object should have the following properties:
  - Index
  - Maximum of 1024 Bytes of Characters as data
  - Prev Hash
  - Current Hash: Based on any cryptographic algorithm, generate a hash. Hash function should include the following parameters as input:
    1. Index
    2. Data
    3. Prev Hash
  - Output: `<Fixed-Length-Hash>`

  **Notes:** The first Block will have 0000 as prevHash.

### Stage 2: Correction State

- A Data Store Object is said to be "Correct" if the generated Hash follows a certain pattern, which is true for all connected objects. For example, the first 4 digits of the Hash are zero.
- Add a `correction_value` field in the object, which will store the additional data. This field's data, when taken into consideration with all the other fields in the object while calculating hash, should produce a hash with our pattern. Note: The pattern can be anything but should be consistent across all objects.
- Write a function to find any particular Object's Correction Value and update that object's Hash with the new hash. Note: Updating any field in a DataObject shall trigger a recalculation of the hash, which shall then trigger recalculation on any further connected DataStores.

## Implementation

Feel Free to Use any Programming language to Code this requirement.
You can also create a UI that shows this functionality in action or it can be a terminal program.
