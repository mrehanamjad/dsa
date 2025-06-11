**Linked List in C++ (Easy Notes)**

### What is a Linked List?
A **linked list** is a data structure used to store a sequence of elements. Unlike arrays, elements in a linked list are not stored in continuous memory locations.

### Why Use Linked List?
- **Dynamic Size**: It can grow or shrink during runtime.
- **Efficient Insert/Delete**: Adding or removing elements is easier compared to arrays.
- **No Wastage of Memory**: Uses only as much memory as needed.

### Types of Linked List
1. **Singly Linked List** – Each node points to the next node.
2. **Doubly Linked List** – Each node points to both previous and next nodes.
3. **Circular Linked List** – The last node connects back to the first node.

### Structure of a Node
A **node** is the basic unit of a linked list. Each node has:
- **Data** (stores value)
- **Pointer** (stores address of next node)

Example in C++:
```cpp
struct Node {
    int data;        // Data part
    Node* next;      // Pointer to the next node
};
```

### Creating a Linked List
1. **Define a Node**
2. **Create Head (Starting Node)**
3. **Link Nodes Together**

Example:
```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

int main() {
    Node* head = new Node();
    Node* second = new Node();
    Node* third = new Node();

    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = nullptr;
    
    return 0;
}
```

### Basic Operations
1. **Insertion** (At beginning, middle, or end)
2. **Deletion** (Remove a node)
3. **Traversal** (Go through the list)

Example: Traversing a Linked List
```cpp
void printList(Node* n) {
    while (n != nullptr) {
        cout << n->data << " ";
        n = n->next;
    }
}
```

### Advantages
- Efficient memory usage
- Fast insertion and deletion

### Disadvantages
- Uses extra memory for pointers
- Slower searching compared to arrays

### Conclusion
Linked lists are useful when we need dynamic memory allocation and efficient insertions/deletions. Understanding its structure and operations will help in mastering data structures in C++!
