from node import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit
  
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("All out of space!")
  
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.next_node
            self.size -= 1
            return item_to_remove.value
        else:
            print("This stack is totally empty.")
  
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Nothing to see here!")
    
    def has_space(self):
        if self.limit > self.size:
            return True
    
    def is_empty(self):
        if self.size == 0:
            return True
    
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