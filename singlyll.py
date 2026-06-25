class Node:
    # A single box: holds data and a link to the next box.
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None      # start of the list

    def append(self, data):
        # Add a node at the end.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:        # walk to the last node
            current = current.next
        current.next = new_node

    def prepend(self, data):
        # Add a node at the front.
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        # Delete the first node matching `data`.
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        # Print the chain: 7 -> 3 -> 9 -> None
        current = self.head
        parts = []
        while current:
            parts.append(str(current.data))
            current = current.next
        parts.append("None")
        print(" -> ".join(parts))


# --- Using it ---
ll = LinkedList()
ll.append(7)
ll.append(3)
ll.append(9)
ll.prepend(1)
ll.display()          # 1 -> 7 -> 3 -> 9 -> None
ll.remove(3)
ll.display() 