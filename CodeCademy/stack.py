from node import Node

class Stack:
    def __init__(self):
        self.top_item = None
  
# Define your push() and pop() methods below:
    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item
  
    def pop(self):
        item_to_remove = self.top_item
        self.top_item = item_to_remove.next_node
        return item_to_remove.value
  
    def peek(self):
        return self.top_item.get_value()
    
    def show(self):
        string = ""
        current_node = self.top_item
        while current_node:
            string += str(current_node.value) + "\n"
            current_node = current_node.next_node
        print(string)
  
test = Stack()
test.push(25)
test.push(12)
test.push(54)
test.show()
print(test.peek())
print(test.pop())