# Stacks

## Overview
A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. Think of it like a stack of plates: you can only add a new plate to the top, and you can only remove the topmost plate. The last plate you put on is the first one you take off.

## Pros
- **Fast Operations**: Both push and pop operations are very fast, taking constant time $(O(1))$, as they only deal with the top of the stack.
- **Simple to Implement**: Stacks can be easily implemented using either an array or a linked list.
- **Efficient Memory Management**: The LIFO principle makes stacks ideal for tasks where you need to manage function calls and local variables.

## Cons
- **Limited Access**: You can only access the element at the top of the stack. To get to an element in the middle or bottom, you must remove all the elements above it.
- **Potential for Stack Overflow**: If you push too many elements onto a stack with a fixed size (like one implemented with an array), you can run out of memory, causing a "stack overflow" error.

## Applications
- **Function Calls**: Compilers and interpreters use a call stack to manage function calls. When a function is called, its state is pushed onto the stack. When the function returns, its state is popped off.
- **Undo/Redo Functionality**: Most software applications use a stack to keep track of user actions.
- **Expression Evaluation**: Stacks are used to evaluate arithmetic expressions (e.g., converting infix expressions to postfix and evaluating them).
- **Recursion**: Recursive algorithms use the call stack implicitly to manage their state at each level of the call.
- **Web Browser History**: A browser's "Back" button functionality can be implemented using a stack.

## Operations
| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Push      | O(1)           | Add an element to the top of the stack |
| Pop       | O(1)           | Remove the element from the top of the stack |
| Peek/Top  | O(1)           | View the top element without removing it |
| isEmpty   | O(1)           | Check if the stack is empty |
| Size      | O(1)           | Get the number of elements in the stack |
| Lookup    | O(n)           | Find an element in the stack (requires popping elements) |

## Implementation
In this repository, we provide two implementations of a stack:
1. **Linked List-based Stack**: Uses nodes with references to implement the stack.
2. **Array-based Stack**: Uses a dynamic array to implement the stack.

Each implementation has its own advantages:
- Linked List implementation never runs out of space (until system memory is exhausted)
- Array implementation may have better memory locality and cache performance