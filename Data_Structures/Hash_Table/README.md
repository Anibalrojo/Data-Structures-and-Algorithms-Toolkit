# Hash Table

## Overview
A hash table (hash map, dictionaries) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. 

## Pros
- Fast operations: average $O(1)$ time complexity for search, insert, and delete
- Flexible keys: can use various data types as keys
- Dynamic size: can grow as needed (in most implementations)
- Efficient for large datasets when properly implemented

## Cons
- Collisions can degrade performance
- May require good hash function design
- Potentially higher memory usage due to unused buckets
- No ordering of elements (unlike ordered maps)
- Worst case performance can be $O(n)$ if many collisions occur

## Applications
- Database indexing
- Caches
- Symbol tables in compilers and interpreters
- Spell checkers
- Dictionaries and sets in programming languages
- Counting frequencies (e.g., word count)
- De-duplication of data

## Operations
| Operation | Average Time | Worst Time | Description |
|-----------|-------------|------------|-------------|
| Insert    | O(1)        | O(n)       | Adding a key-value pair |
| Delete    | O(1)        | O(n)       | Removing a key-value pair |
| Search    | O(1)        | O(n)       | Finding a value by key |
| Resize/Rehash | O(n)    | O(n)       | Increasing table size and redistributing entries |

## Implementation
The core of the implementation involves:
- A **hash function** to map keys to an index in the list. A good hash function should distribute keys uniformly across the table to minimize collisions.
- A **collision resolution** method when multiple keys map to the same index. The most common method it's called **separated chaining**, where each index of the main array points to a secondary data structure, like in this case, a list. This method origins the concepts of **pointers** and **linked lists**.

## Note
This hash table Python implementation was made using lists of lists, instead of the built-in dictionary data structure. This decision was made to focus on key-value mapping and collision handling.
1. The outer list represents your buckets (fixed size array)
2. Each inner list represents a chain of key-value pairs for collision resolution
3. This structure directly models the separate chaining collision resolution strategy 

