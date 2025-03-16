class Node:
    """
    Represents a node in a circular linked list.
    Each node contains a value (data) and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data  # Value stored in the node
        self.next = None  # Reference to the next node


class CircularList:
    """
    Implements a circular linked list.
    Allows operations such as adding, removing, searching, and displaying elements.
    """
    def __init__(self):
        self.head = None  # Reference to the first node of the list

    def is_empty(self):
        """
        Checks if the list is empty.
        Returns True if empty, otherwise False.
        """
        return self.head is None

    def add(self, data):
        """
        Adds an element to the end of the list.
        If the list is empty, the new node references itself, making it circular.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head  # Points to itself, making the list circular
        else:
            current_node = self.head
            while current_node.next != self.head:  # Traverses to the last node
                current_node = current_node.next
            current_node.next = new_node  # Connects the last node to the new node
            new_node.next = self.head  # Closes the cycle

    def add_at_start(self, data):
        """
        Adds an element to the beginning of the list.
        Updates the head reference and adjusts nodes to maintain circularity.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head  # New node points to the current head
            current_node = self.head
            while current_node.next != self.head:  # Traverses to the last node
                current_node = current_node.next
            current_node.next = new_node  # The last node points to the new node
            self.head = new_node  # Updates the head to the new node

    def remove_last(self):
        """
        Removes the last element from the list.
        If the list has only one element, it will be emptied.
        """
        if self.is_empty():
            print("The list is empty.")
            return

        if self.head.next == self.head:  # Special case: only one element
            print(f"Element {self.head.data} removed.")
            self.head = None
            return

        current = self.head
        previous = None

        while current.next != self.head:  # Traverses to the last node
            previous = current
            current = current.next

        previous.next = self.head  # Removes the reference to the last node
        print(f"Element {current.data} removed.")

    def remove_first(self):
        """
        Removes the first element from the list.
        If the list has only one element, it will be emptied.
        """
        if self.is_empty():
            print("The list is empty.")
            return

        if self.head.next == self.head:  # Special case: only one element
            print(f"Element {self.head.data} removed.")
            self.head = None
            return

        print(f"Element {self.head.data} removed.")
        last = self.head
        while last.next != self.head:  # Traverses to the last node
            last = last.next
        self.head = self.head.next  # Updates the head to the next node
        last.next = self.head  # Closes the cycle with the new head

    def search(self, data):
        """
        Searches for an element in the list.
        Returns True if the element is found, otherwise False.
        """
        if self.is_empty():
            return False
        current = self.head
        while True:
            if current.data == data:  # Checks the current value
                return True
            current = current.next
            if current == self.head:  # Returns to the start, ending the search
                break
        return False

    def size(self):
        """
        Calculates and returns the number of elements in the list.
        """
        if self.is_empty():
            return 0
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:  # Returns to the start, ending the count
                break
        return count

    def display_list(self):
        """
        Displays all elements in the circular list.
        Shows that the list is circular by displaying the first element at the end.
        """
        if self.is_empty():
            print('The list is empty.')
            return

        current = self.head
        print(current.data, end=' -> ')  # Displays the first node's data
        current = current.next

        while current != self.head:  # Continues until returning to the first node
            print(current.data, end=' -> ')
            current = current.next

        print(f'({self.head.data})')  # Shows the first element to indicate circularity


# Testing the Circular List
list = CircularList()

# Adding elements
list.add(10)
list.add(20)
list.add(30)
print("List after additions:")
list.display_list()

# Adding an element at the start
list.add_at_start(5)
print("\nList after adding 5 at the start:")
list.display_list()

# Removing the last element
list.remove_last()
print("\nList after removing the last element:")
list.display_list()

# Removing the first element
list.remove_first()
print("\nList after removing the first element:")
list.display_list()

# Removing all elements
list.remove_first()
list.remove_first()
print("\nList after removing all elements:")
list.display_list()
