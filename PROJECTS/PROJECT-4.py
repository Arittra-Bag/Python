class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def display(self):
        if self.top is None:
            print("Stack is empty!")
        else:
            print("Stack:")
            current = self.top
            stack_items = []
            while current:
                stack_items.append(current.data)
                current = current.next
            for item in stack_items:
                print(item)

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def display(self):
        if self.front is None:
            print("Queue is empty!")
        else:
            print("Queue:",end="")
            current = self.front
            queue_items = []
            while current:
                queue_items.append(current.data)
                current = current.next
            print(" ".join(queue_items))

def main():
    stack = Stack()
    queue = Queue()
    while True:
        print("\nMenu:\n1. Push (Stack)\n2. Pop (Stack)\n3. Enqueue (Queue)\n4. Dequeue (Queue)\n5. Display (Stack)\n6. Display (Queue)\n7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter data to push: ")
            stack.push(data)
        elif choice == 2:
            data = stack.pop()
            if data is not None:
                print("Popped data:", data)
            else:
                print("Stack Underflow!")
        elif choice == 3:
            data = input("Enter data to enqueue: ")
            queue.enqueue(data)
        elif choice == 4:
            data = queue.dequeue()
            if data is not None:
                print("Dequeued data:", data)
            else:
                print("Queue Underflow!")
        elif choice == 5:
            stack.display()
        elif choice == 6:
            queue.display()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()