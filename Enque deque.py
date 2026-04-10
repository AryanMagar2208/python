class Stack:
    def __init__(self):
        self.stack = []
        
    def enque(self, item):   
        self.stack.append(item)
        print(item, "pushed into stack")
        
    def deque(self):        
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop")
            return None
        else:
            return self.stack.pop()
        
    def display(self):
        print("Stack elements:", self.stack)
        

s = Stack()

while True:
    print("\n1. Enque")
    print("2. Deque")
    print("3. Display")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = input("Enter item to enque: ")
        s.enque(item)
        
    elif choice == 2:
        popped = s.deque()
        if popped is not None:
            print(popped, "popped from stack")
            
    elif choice == 3:
        s.display()
        
    elif choice == 4:
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice!")