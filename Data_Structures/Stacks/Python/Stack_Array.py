"""
Stack Implementation using Array

This module provides a Stack implementation using a Python list (dynamic array).
"""


class Stack:
    """
    Stack implementation using a Python list.
    
    This implementation follows the Last-In-First-Out (LIFO) principle.
    Python lists automatically handle resizing, so this implementation
    doesn't have a fixed size limit.
    """
    def __init__(self):
        """Initialize an empty Stack."""
        self.stack = []

    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def push(self, item):
        """
        Add an element to the top of the stack.
        
        Args:
            item: The item to add to the stack.
            
        Time Complexity:
            O(1) amortized, occasionally O(n) when the list needs to resize.
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove and return the top element from the stack.
        
        Returns:
            The item from the top of the stack.
            
        Raises:
            IndexError: If the stack is empty.
            
        Time Complexity:
            O(1)
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.stack.pop()  # Return the last item (LIFO)

    def peek(self):
        """
        View the top element without removing it.
        
        Returns:
            The item at the top of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.stack[-1]

    def get_size(self):
        """
        Get the number of elements in the stack.
        
        Returns:
            int: The number of elements in the stack.
        """
        return len(self.stack)

    def __str__(self):
        """
        Return a string representation of the stack.
        
        Returns:
            str: A string showing the stack elements from top to bottom.
        """
        if self.is_empty():
            return "Empty Stack"
        return "TOP -> " + " -> ".join(map(str, reversed(self.stack))) + " -> None"


# Example usage
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()
    print("New stack:", stack)
    
    # Push elements
    print("\nPushing elements:")
    stack.push("apple")
    stack.push("banana")
    stack.push("cherry")
    print("Stack after pushing 'apple', 'banana', 'cherry':", stack)
    print("Size:", stack.get_size())
    
    # Peek at top element
    print("\nTop element (peek):", stack.peek())
    
    # Pop elements
    print("\nPopping elements:")
    print("Popped:", stack.pop())
    print("Stack after pop:", stack)
    print("Popped:", stack.pop())
    print("Stack after pop:", stack)
    
    # Check if empty
    print("\nIs stack empty?", stack.is_empty())
    
    # Pop last element
    print("\nPopping last element:", stack.pop())
    print("Is stack empty?", stack.is_empty())
