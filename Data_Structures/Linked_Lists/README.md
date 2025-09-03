# Linked Lists

## Overview
A linked list is a linear data structure where elements are not stored in contiguous memory locations, making them more flexible for dynamic memory allocation. There are a collection of individual units called nodes, where each node contains the data and a **pointer** (or reference) to the next node in the sequence. A pointer is simply a reference to another place in memory, which links the nodes together. The start of the list is called the head, and the end is a node that points to null. 

Unlike an array where elements are indexed and easily accessed, traversing a linked list requires you to start at the head and follow the pointers from one node to the next.

It's important to note that the most common method for resolving collisions is **separate chaining**:
- In this approach, each slot of the hash table's array doesn't store a single key-value pair but instead stores a **pointer** to a **linked list**.
- When a collision occurs, the new key-value pair is simply added as a new node to the linked list at that array index.
- This allows multiple items to coexist at the same index without overwriting each other, but a large number of collisions at one index can cause the linked list to grow long, which can degrade performance from $O(1)$ to $O(n)$ for that specific bucket.


## Pros
- **Dynamic size**: can grow or shrink as needed during execution 
- **Efficient Insertion/Deletion**: $O(1)$ if position is known
- No memory wastage as size can grow or shrink as needed
- No need for initial size declaration
- **Ordered Data**: The elements in a linked list have a defined order, as each node points to the next one. This is in contrast to hash tables, which do not maintain order.

## Cons
- **Slow Access/Lookup**: You cannot access an element by its index. To find an element, you must traverse the list from the beginning, resulting in a time complexity of **$O(n)$**. Arrays are faster for lookups due to **cache locality**, where elements stored close together in memory can be accessed more quickly
- **Extra memory** required for storing pointers. Higher memory usage per element compared to arrays
- Not cache-friendly due to non-contiguous memory allocation
- Reverse traversal is difficult in singly linked lists

## Applications
- Implementation of stacks and queues
- Dynamic memory allocation
- Representing sparse matrices
- Hash tables (chaining for collision resolution)
- Undo functionality in applications
- Music playlists
- Browser history navigation

## Operations
| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Access by index (`lookup`)    | O(n)           | Retrieving an element at a given position |
| Search (`find`)    | O(n)           | Finding an element in the list |
| Insertion at beginning (`preppend`) | O(1) | Adding a new element at the start |
| Insertion at end (`append`) | O(1) or O(n) | Adding a new element at the end (O(1) with tail pointer) |
| Insertion in middle (`insert`) | O(n) | Adding a new element at a specific position |
| Deletion at beginning (`pop_first`)| O(1) | Removing the first element |
| Deletion at end (`pop`) | O(n) | Removing the last element |
| Deletion in middle | O(n) | Removing an element from a specific position |
