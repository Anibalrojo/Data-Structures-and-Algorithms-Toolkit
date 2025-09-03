# Array

## Overview
An array is a collection of elements stored at contiguous memory locations. It is the simplest data structure where each element can be accessed using an index. Arrays are of fixed size and allocated during compile time.

## Pros
- Simple to implement and use
- **Fast access**: because elements are stored in continuous blocks of memory, you can access any element directly using it's index (O(1) time complexity)
- Good cache locality which leads to better performance
- **Memory efficient**: arrays only store the data and minimal metadata. They don't require any extra memory overhead to store links or pointers between elements

## Cons
- Fixed size in many programming languages
- Inefficient Insertion/Deletion: inserting or deleting an element from the middle of an array requires shifting all subsequent elements (O(n) time complexity)
- Inefficient memory usage if the size is not known in advance
- Cannot store elements of different data types (in most languages)

## Applications
- Storing and accessing sequential data
- Temporary storage of objects in memory
- Implementation of other data structures like `Stacks`, `Queues`, `Heaps`, `Hash tables`
- Lookup tables and buffers: Arrays are perfect for creating lookup tables where you need to quickly retrieve data based on a key (e.g., a simple database of product prices where the index is the product ID)
- Matrix operations in graphics, scientific computing
- Sorting algorithms like `Bubble Sort`, `Quick Sort`, and `Merge Sort`

## Operations
| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Access    | O(1)           | Retrieving an element at a given index |
| Search    | O(n)           | Finding an element in the array |
| Insertion | O(n)           | Adding an element at a specific position |
| Deletion  | O(n)           | Removing an element from the array |
| Traversal | O(n)           | Visiting each element in the array |
