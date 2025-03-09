import java.util.*;

public class Main {
    public static void main(String[] args) {
        // creating queues
        Queue<String> regularOrders = new LinkedList<>();
        Queue<String> priorityOrders = new LinkedList<>();

        // Testing adding
        addRegularOrder(regularOrders, "Pizza");
        addRegularOrder(regularOrders, "Sushi");
        addRegularOrder(regularOrders, "Apple");
        addPriorityOrder(priorityOrders, "Water");
        addPriorityOrder(priorityOrders, "Rice");
        displayList(regularOrders, priorityOrders);

        // Testing Removing
        removeOrder(regularOrders, priorityOrders, "Apple");
        displayList(regularOrders, priorityOrders);

        // Testing Processing
        String processedOrder = processNewOrder(regularOrders, priorityOrders);
        System.out.println(processedOrder + " has been process");
        displayList(regularOrders, priorityOrders);

        // Testing if exists
        boolean exist = orderExists(regularOrders, "Apple");
        if (exist) {
            System.out.println("Exists");
        } else {
            System.out.println("Not Exists");
        }
        boolean exist2 = orderExists(regularOrders, "Pizza");
        if (exist2) {
            System.out.println("Exists");
        } else {
            System.out.println("Not Exists");
        }

    }

    // Adds a new order to the regular queue.
    static void addRegularOrder(Queue<String> queue, String order) {
        queue.add(order);
    }

    // Adds a new order to the priority queue.
    static void addPriorityOrder(Queue<String> priorityQueue, String order) {
        priorityQueue.add(order);
    }

    // Processes the next available order, prioritizing priority orders first.
    static String processNewOrder(Queue<String> regular, Queue<String> priority) {
        // Check priority queue to make priority order get process first
        if (!priority.isEmpty()) {
            return priority.poll();
        }

        // If priority queue is empty then regular queue order will be process
        else if (!regular.isEmpty()) {
            return regular.poll();
        } else {
            return null;
        }
    }

    // Removes an order from either queue if found. Returns a boolean to show
    static boolean removeOrder(Queue<String> regular, Queue<String> priority, String order) {
        for (String eachOrder : priority) {
            if (eachOrder == order) {
                priority.remove(order);
                System.out.println(order + " has been removed");
                return true;
            }
        }
        ;

        for (String eachOrder : regular) {
            if (eachOrder == order) {
                regular.remove(order);
                System.out.println(order + " has been removed");
                return true;
            }
        }
        ;

        return false;
    }

    // Displays all orders, showing priority orders first.
    static void displayList(Queue<String> regular, Queue<String> priority) {
        System.out.println("\n===== Orders =====");
        System.out.println("Priority Orders : ");
        for (String order : priority) {
            System.out.println(order);
        }
        System.out.println("\nRegular Orders : ");
        for (String order : regular) {
            System.out.println(order);
        }
        System.out.println("==================\n");
    }

    // Uses recursion to check if an order exists in either queue.
    static boolean orderExists(Queue<String> checkingQueue, String order) {
        Queue<String> tempQueue = new LinkedList<>(checkingQueue);
        if (tempQueue.isEmpty()) {
            return false;
        }
        if (tempQueue.poll().equals(order)) {
            return true;
        }
        return orderExists(tempQueue, order);
    }
}