class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")
        
    def safe_pop(self):
        if len(self.stack) == 0:
            print("stack is empty, nothing to pop")
            return None
        else:
            return self.stack.pop()
        
    def display(self):
        print("stack elements:", self.stack)
        
s = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    
    choice = int(input("enter your choice: "))
    
    if choice == 1:
        item = input("Enter item to push: ")
        s.push(item)
        
    elif choice == 2:
        popped = s.safe_pop()
        if popped is not None:
            print(popped, "popped from stack")
            
    elif choice == 3:
        s.display()
        
    elif choice == 4:
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice!")