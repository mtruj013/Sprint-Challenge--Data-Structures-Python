class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):

        current = self.head

        # if its empty
        if not current:
            return
        
        # while theres something after the head
        while current.next_node:
            # store the next node 
            temp = current.next_node
            # switch positions
            current.next_node = prev
            # move along the line
            prev = current
            current = temp
        # since theres nothing after the last current, set the next node to prev which is none
        current.next_node = prev

        self.head = current
            
        

