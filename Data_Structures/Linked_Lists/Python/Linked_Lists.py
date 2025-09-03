"""
Linked List Implementation

This module provides a comprehensive implementation of a Singly Linked List data structure.
A linked list is a linear data structure where elements are stored in nodes, and each node
points to the next node in the sequence.
"""

class Node:
    """
    A Node in a Linked List.
    
    Each node contains data and a reference to the next node in the sequence.
    
    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the linked list.
    """
    def __init__(self, data):
        """
        Initialize a new Node.
        
        Args:
            data: The data to store in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Singly Linked List implementation.
    
    A linked list is a linear data structure where elements are stored in nodes,
    and each node points to the next node in the sequence.
    
    Attributes:
        head: Reference to the first node in the list.
        tail: Reference to the last node in the list.
        length: Number of nodes in the list.
    """
    def __init__(self):
        """Initialize an empty Linked List."""
        self.head = None
        self.tail = None
        self.length = 0

    def _init_first_node(self, new_node):
        """
        Initialize the list when it's empty.
        
        Args:
            new_node: The first node to add to the empty list.
        """
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, data):
        """
        Add a node to the end of the list.
        
        Args:
            data: The data to store in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self._init_first_node(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        """
        Add a node to the beginning of the list.
        
        Args:
            data: The data to store in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self._init_first_node(new_node)
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        """Print the list in list format: [a, b, c]"""
        elements = []
        current = self.head

        if self.head == None:
            print('Empty List')
        else:
            while current:
                elements.append(current.data)
                current = current.next
            print(elements)

    def insert(self, index, data):
        """
        Insert a node at a specific position.
        
        Args:
            index: The position to insert the node (0-based).
            data: The data to store in the new node.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        if index == 0:
            return self.prepend(data)
        if index == self.length:
            return self.append(data)

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        # New node points to the node that was originally after current
        new_node.next = current.next

        # Current node now points to the new node
        current.next = new_node
        self.length += 1

    def lookup(self, index):
        """
        Return the value at a specific position.
        
        Args:
            index: The position to look up (0-based).
            
        Returns:
            The data at the specified position.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __len__(self):
        """
        Allow using len(list).
        
        Returns:
            int: The number of nodes in the list.
        """
        return self.length

    def __repr__(self):
        """
        Official representation of the list, allows using print().
        
        Returns:
            str: String representation of the list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return str(elements)

    def find(self, value):
        """
        Find a value and return the index of its first occurrence.
        
        Args:
            value: The value to search for.
            
        Returns:
            int: The index of the first occurrence, or -1 if not found.
        """
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def pop(self):
        """
        Remove and returns the last node.
        
        Returns:
            The data of the removed node.
            
        Raises:
            IndexError: If the list is empty.
        """
        if self.head is None:
            raise IndexError("List is empty")
        if self.length == 1:
            value = self.head.data
            self.head = None
            self.tail = None
            self.length = 0
            return value

        current = self.head
        while current.next != self.tail:
            current = current.next
        value = self.tail.data
        current.next = None
        self.tail = current
        self.length -= 1
        return value

    def pop_first(self):
        """
        Remove and returns the first node.
        
        Returns:
            The data of the removed node.
            
        Raises:
            IndexError: If the list is empty.
        """
        if self.head is None:
            raise IndexError("List is empty")
        value = self.head.data
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return value

    def clear(self):
        """Remove all elements from the list."""
        self.head = None
        self.tail = None
        self.length = 0

    def reverse(self):
        """Reverse the order of nodes in the list."""
        prev = None
        current = self.head
        self.tail = self.head          # Current head will be tail after reversal
        while current:
            next_node = current.next   # Save reference to the next node
            current.next = prev        # Reverse the link
            prev = current             # Move prev to current node
            current = next_node        # Move current to original next node
        self.head = prev               # The last visited node becomes the new head

    def to_list(self):
        """
        Convert to a Python list.
        
        Returns:
            list: A Python list containing all elements.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def is_empty(self):
        """
        Check if the list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.length == 0

    def extend(self, iterable):
        """
        Add all elements from an iterable to the end of the list.
        
        Args:
            iterable: An iterable containing elements to add.
        """
        for item in iterable:
            self.append(item)


# Example usage
if __name__ == "__main__":
    # Create a new linked list
    print("Step 1: Creating a new linked list")
    linked_list = LinkedList()
    print(f"Empty list: {linked_list}")
    print(f"Is empty: {linked_list.is_empty()}")
    
    # Add elements to the list
    print("\nStep 2: Adding elements")
    linked_list.append("apple")
    linked_list.append("banana")
    linked_list.prepend("orange")
    print(f"List after adding elements: {linked_list}")
    print(f"Length: {len(linked_list)}")
    
    # Insert at specific position
    print("\nStep 3: Inserting at specific position")
    linked_list.insert(2, "grape")
    print(f"List after inserting 'grape' at index 2: {linked_list}")
    
    # Access elements
    print("\nStep 4: Accessing elements")
    print(f"Element at index 1: {linked_list.lookup(1)}")
    
    # Search for elements
    print("\nStep 5: Searching for elements")
    print(f"Index of 'banana': {linked_list.find('banana')}")
    print(f"Index of 'mango': {linked_list.find('mango')}")  # Should return -1
    
    # Remove elements
    print("\nStep 6: Removing elements")
    popped = linked_list.pop()
    print(f"Popped element from end: {popped}")
    print(f"List after pop: {linked_list}")
    
    popped_first = linked_list.pop_first()
    print(f"Popped element from beginning: {popped_first}")
    print(f"List after pop_first: {linked_list}")
    
    # Reverse the list
    print("\nStep 7: Reversing the list")
    linked_list.reverse()
    print(f"Reversed list: {linked_list}")
    
    # Convert to Python list
    print("\nStep 8: Converting to Python list")
    py_list = linked_list.to_list()
    print(f"As Python list: {py_list}")
    
    # Extend with multiple elements
    print("\nStep 9: Extending with multiple elements")
    linked_list.extend(["cherry", "date", "elderberry"])
    print(f"After extending: {linked_list}")
    
    # Clear the list
    print("\nStep 10: Clearing the list")
    linked_list.clear()
    print(f"After clearing: {linked_list}")
    print(f"Is empty: {linked_list.is_empty()}")