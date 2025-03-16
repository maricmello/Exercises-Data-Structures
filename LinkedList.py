class Node:
    """
    Represents a node in a linked list.
    Each node contains a value (data) and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data  # Value stored in the node
        self.next = None  # Reference to the next node (initially None)

class LinkedList:
    """
    Class that implements a linked list.
    Allows operations such as adding, removing, searching, and displaying elements.
    """
    def __init__(self):
        self.head = None  # Starting point of the list (first node)

    def is_empty(self):
        """
        Checks if the list is empty.
        Returns True if empty, otherwise False.
        """
        return self.head is None

    def add(self, data):
        """
        Adds a new element to the end of the list.
        
        Parameter:
        - data: Value to be added to the list.
        """
        new_node = Node(data)
        if not self.head:  # Special case: empty list
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:  # Traverses to the last node
            current_node = current_node.next
        current_node.next = new_node  # Connects the new node to the end of the list

    def add_at_start(self, data):
        """
        Adds a new element at the start of the list.
        """
        new_node = Node(data)
        new_node.next = self.head  # The new node points to the old start
        self.head = new_node  # Updates the head to the new node

    def add_at_position(self, data, position):
        """
        Adds a new element at a specific position.
        
        Parameters:
        - data: Value to be added.
        - position: Index where the element will be inserted.
        """
        new_node = Node(data)

        if position == 0:  # Special case: insert at the start
            self.add_at_start(data)
            return

        current = self.head
        counter = 0

        while current is not None and counter < position - 1:
            current = current.next
            counter += 1

        if current is not None:  # Inserts at the found position
            new_node.next = current.next
            current.next = new_node
        else:
            print(f'Position {position} out of range.')

    def remove_last(self):
        """
        Removes the last element of the list.
        """
        if self.is_empty():  # Special case: empty list
            print('The list is empty.')
            return

        current = self.head
        previous = None

        while current.next is not None:  # Traverses to the last node
            previous = current
            current = current.next

        if previous is None:  # Special case: only one element in the list
            self.head = None
        else:
            previous.next = None  # Removes the reference to the last node

        print(f'Element {current.data} removed.')

    def remove_first(self):
        """
        Removes the first element of the list.
        """
        if self.is_empty():  # Special case: empty list
            print('The list is empty.')
            return

        print(f'Element {self.head.data} removed.')
        self.head = self.head.next  # Updates the head to the next node

    def remove_at_position(self, position):
        """
        Removes the element at a specific position.
        
        Parameter:
        - position: Index of the element to be removed.
        """
        if self.is_empty():  # Special case: empty list
            print('The list is empty.')
            return

        if position == 0:  # Special case: remove the first element
            self.remove_first()
            return

        current = self.head
        previous = None
        counter = 0

        while current is not None and counter < position:
            previous = current
            current = current.next
            counter += 1

        if current is not None:  # Removes the reference to the node at the position
            previous.next = current.next
            print(f'Element at position {position} removed.')
        else:
            print(f'Position {position} out of range.')

    def search(self, data):
        """
        Searches for an element in the list.
        
        Parameter:
        - data: Value to be searched.
        
        Returns:
        - True if the element is found, False otherwise.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def size(self):
        """
        Returns the size of the list (number of elements).
        """
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next
        return counter

    def search_at_position(self, position):
        """
        Returns the element at a specific position.
        
        Parameter:
        - position: Index of the element.
        """
        current = self.head
        counter = 0

        while current is not None and counter < position:
            current = current.next
            counter += 1

        if current is not None:
            print(f'Element at position {position}: {current.data}')
        else:
            print(f'Position {position} out of range.')

    def display_list(self):
        """
        Displays all the elements of the list, separated by "->".
        """
        if self.is_empty():  # Special case: empty list
            print("The list is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=' -> ')
                current = current.next
            print('None')  # Marks the end of the list

    def __iter__(self):
        """
        Makes the list iterable, allowing it to be used in for loops.
        """
        current = self.head
        while current is not None:
            yield current.data  # Returns the value of the current node
            current = current.next


# Testing the Linked List
list = LinkedList()
list.add(1)
list.add(2)
list.add(3)

for element in list:  # Iterates over the elements using __iter__
    print(element)
