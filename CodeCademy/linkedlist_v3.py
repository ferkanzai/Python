# We'll be using our Node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

# Our LinkedList class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        print(string_list)

# Define your remove_node method below:

    def remove_node(self, value_to_remove):
        current_node = self.head_node

        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                #print(current_node.value)
                current_next_node = current_node.get_next_node()
                #print(current_next_node.value)
                if current_next_node.get_value() == value_to_remove:
                    current_node.next_node = current_next_node.get_next_node()
                    #print(current_next_node.value)
                    current_node = None
                else:
                    current_node = current_next_node
    
    def remove_multiple(self, value_to_remove):
        current_node = self.head_node
        #print(current_node.get_value())

        while current_node.next_node:
            current_next_node = current_node.get_next_node()

            if self.head_node.get_value() == value_to_remove:
                self.head_node = self.head_node.next_node
            
            #print(current_next_node.get_value())
            if current_next_node.get_value() == value_to_remove:
                current_node.next_node = current_node.next_node.next_node
            current_node = current_node.next_node
            

ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(90)
ll.insert_beginning(5675)
ll.insert_beginning(70)
ll.insert_beginning(90)
ll.insert_beginning(70)
ll.stringify_list()
#ll.remove_node(5675)
ll.remove_multiple(70)
ll.stringify_list()
ll.remove_multiple(90)
ll.stringify_list()
ll.remove_node(5)
ll.stringify_list()