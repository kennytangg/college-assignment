import java.util.*;

// Node class for Singly Linked List
class Node {
    int data;
    Node next;

    // Constructor
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// Singly Linked List
class SingleLinkedList {
    private Node head;
    private int size;

    // Constructor
    public SingleLinkedList() {
        this.head = null;
        this.size = 0; // track the size of the list / number of nodes
    }

    // Add element at the beginning of the list
    public void addFirst(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
        size++;
    }

    // Add element at the end of the list
    public void addLast(int data) {
        Node newNode = new Node(data);

        // If list is empty, make new node the head
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            // Loop until the final node in the list
            while (current.next != null) {
                current = current.next;
            }
            // Add new node at the end of the list
            current.next = newNode;
        }
        size++;
    }

    // Add element at specific position
    public void add(int position, int data) {
        // Ensures position is within range
        if (position < 0 || position > size) {
            throw new IndexOutOfBoundsException("Position: " + position + ", Size: " + size);
        }

        // If adding at the beginning
        if (position == 0) {
            addFirst(data);
            return;
        }

        // If adding at the end
        if (position == size) {
            addLast(data);
            return;
        }

        // Create new node
        Node newNode = new Node(data);

        // Find the node at position-1
        Node current = head;
        for (int i = 0; i < position - 1; i++) {
            current = current.next;
        }

        // Insert new node
        newNode.next = current.next;
        current.next = newNode;
        size++;
    }

    // Remove first element
    public int removeFirst() {
        if (head == null) {
            throw new NoSuchElementException("List is empty");
        }

        int data = head.data;
        head = head.next;
        size--;
        return data;
    }

    // Remove last element
    public int removeLast() {
        if (head == null) {
            throw new NoSuchElementException("List is empty");
        }

        // If only one element
        if (head.next == null) {
            int data = head.data;
            head = null;
            size--;
            return data;
        }

        // Find the second last node
        Node current = head;
        while (current.next.next != null) {
            current = current.next;
        }

        // Remove the last node
        int data = current.next.data;
        current.next = null;
        size--;
        return data;
    }

    // Remove element at specific position
    public int remove(int position) {
        // Ensures position is within range
        if (position < 0 || position >= size) {
            throw new IndexOutOfBoundsException("Position: " + position + ", Size: " + size);
        }

        // If removing first element
        if (position == 0) {
            return removeFirst();
        }

        // If removing last element
        if (position == size - 1) {
            return removeLast();
        }

        // Find the node at position-1
        Node current = head;
        for (int i = 0; i < position - 1; i++) {
            current = current.next;
        }

        // Remove the node at position
        int data = current.next.data;
        current.next = current.next.next;
        size--;
        return data;
    }

    // Get the data at specific position
    public int getData(int position) {
        // Ensures position is within range
        if (position < 0 || position >= size) {
            throw new IndexOutOfBoundsException("Position: " + position + ", Size: " + size);
        }

        Node current = head;
        for (int i = 0; i < position; i++) {
            current = current.next;
        }

        return current.data;
    }

    // Get the size of the list
    public int getSize() {
        return this.size;
    }

    // Check if list contains a value
    public boolean contains(int data) {
        Node current = head;
        while (current != null) {
            if (current.data == data) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    // Print the list
    public void printList() {
        Node current = head;
        System.out.print("List: ");
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}

// Node class for Doubly Linked List
class DoublyNode {
    int data;
    DoublyNode next;
    DoublyNode prev;

    // Constructor
    public DoublyNode(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

// Doubly Linked List
class DoublyLinkedList {
    private DoublyNode head;
    private DoublyNode tail;
    private int size;

    // Constructor
    public DoublyLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    // Add element at the beginning of the list
    public void addFirst(int data) {
        DoublyNode newNode = new DoublyNode(data);

        // If list is empty
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
        size++;
    }

    // Add element at the end of the list
    public void addLast(int data) {
        DoublyNode newNode = new DoublyNode(data);

        // If list is empty
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }

    // Add element at specific position
    public void add(int position, int data) {
        // Ensures position is within range
        if (position < 0 || position > size) {
            throw new IndexOutOfBoundsException("Position: " + position + ", Size: " + size);
        }

        // If adding at the beginning
        if (position == 0) {
            addFirst(data);
            return;
        }

        // If adding at the end
        if (position == size) {
            addLast(data);
            return;
        }

        // Create new node
        DoublyNode newNode = new DoublyNode(data);

        // Find the node at position
        DoublyNode current = head;
        for (int i = 0; i < position; i++) {
            current = current.next;
        }

        // Insert new node before current
        newNode.next = current;
        newNode.prev = current.prev;
        current.prev.next = newNode;
        current.prev = newNode;
        size++;
    }

    // Remove first element
    public int removeFirst() {
        if (head == null) {
            throw new NoSuchElementException("List is empty");
        }

        int data = head.data;

        // If only one element
        if (head == tail) {
            head = null;
            tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }
        size--;
        return data;
    }

    // Remove last element
    public int removeLast() {
        if (tail == null) {
            throw new NoSuchElementException("List is empty");
        }

        int data = tail.data;

        // If only one element
        if (head == tail) {
            head = null;
            tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }
        size--;
        return data;
    }

    // Remove element at specific position
    public int remove(int position) {
        if (position < 0 || position >= size) {
            throw new IndexOutOfBoundsException("Position: " + position + ", Size: " + size);
        }

        // If removing first element
        if (position == 0) {
            return removeFirst();
        }

        // If removing last element
        if (position == size - 1) {
            return removeLast();
        }

        // Find the node at position
        DoublyNode current = head;
        for (int i = 0; i < position; i++) {
            current = current.next;
        }

        // Remove the node
        current.prev.next = current.next;
        current.next.prev = current.prev;
        int data = current.data;
        size--;
        return data;
    }

    // Get element at specific position
    public int getData(int position) {
        // Ensures position is within range
        if (position < 0 || position >= size) {
            throw new IndexOutOfBoundsException("Position: " + position + ", Size: " + size);
        }

        DoublyNode current;

        // Decide whether to start from head or tail
        if (position < size / 2) {
            current = head;
            for (int i = 0; i < position; i++) {
                current = current.next;
            }
        } else {
            current = tail;
            for (int i = size - 1; i > position; i--) {
                current = current.prev;
            }
        }

        return current.data;
    }

    // Check if list contains a value
    public boolean contains(int data) {
        DoublyNode current = head;
        while (current != null) {
            if (current.data == data) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    // Get the size of the list
    public int getSize() {
        return size;
    }

    // Print the list
    public void printList() {
        DoublyNode current = head;
        System.out.print("Forward: ");
        while (current != null) {
            System.out.print(current.data + " <-> ");
            current = current.next;
        }
        System.out.println("null");
    }
}

// Driver
public class LinkedList {
    public static void main(String[] args) {
        System.out.println("Singly Linked List Example:");
        SingleLinkedList sll = new SingleLinkedList();
        sll.addLast(10);
        sll.addLast(20);
        sll.addFirst(5);
        sll.add(2, 15);
        sll.printList();
        System.out.println("Size: " + sll.getSize());
        System.out.println("Element at position 2: " + sll.getData(2));
        System.out.println("Contains 15? " + sll.contains(15));
        System.out.println("Removed element: " + sll.remove(1));
        sll.printList();

        System.out.println("\nDoubly Linked List Example:");
        DoublyLinkedList dll = new DoublyLinkedList();
        dll.addLast(10);
        dll.addLast(20);
        dll.addFirst(5);
        dll.add(2, 15);
        dll.printList();
        System.out.println("Size: " + dll.getSize());
        System.out.println("Element at position 2: " + dll.getData(2));
        System.out.println("Contains 15? " + dll.contains(15));
        System.out.println("Removed element: " + dll.remove(1));
        dll.printList();
    }
}
