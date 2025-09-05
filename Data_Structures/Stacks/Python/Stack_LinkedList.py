"""
Stack Implementation using Linked List

This module provides a Stack implementation using a linked list structure.
"""


class Node:
    """
    A Node in the Stack.
    
    Each node contains data and a reference to the next node.
    """
    def __init__(self, data):
        """
        Initialize a new Node.
        
        Args:
            data: The data to store in the node.
        """
        self.data = data
        self.next = None


class Stack:
    """
    Stack implementation using a linked list.
    
    This implementation follows the Last-In-First-Out (LIFO) principle.
    """
    def __init__(self):
        """Initialize an empty Stack."""
        self.top = None
        self.bottom = None
        self.size = 0

    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.top is None

    def get_size(self):
        """
        Get the number of elements in the stack.
        
        Returns:
            int: The number of elements in the stack.
        """
        return self.size

    def push(self, data):
        """
        Add an element to the top of the stack.
        
        Args:
            data: The data to add to the stack.
        """
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top  # Store reference to current top node
            self.top = new_node       # Update the top node
        self.size += 1

    def pop(self):
        """
        Remove and return the top element from the stack.
        
        Returns:
            The data from the top node.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError('Stack is empty')

        # Save reference to the top node
        popped_node = self.top

        # Move the pointer to the next node, disconnecting the top node
        self.top = self.top.next
        self.size -= 1

        if self.is_empty():
            self.bottom = None
            
        return popped_node.data

    def peek(self):
        """
        View the top element without removing it.
        
        Returns:
            The data from the top node.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.top.data

    def __str__(self):
        """
        Return a string representation of the stack.
        
        Returns:
            str: A string showing the stack elements from top to bottom.
        """
        if self.is_empty():
            return "Empty Stack"
        
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return "TOP -> " + " -> ".join(elements) + " -> None"


# Example usage
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()
    print("New stack:", stack)
    
    # Push elements
    print("\nPushing elements:")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushing 10, 20, 30:", stack)
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
