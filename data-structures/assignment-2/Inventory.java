import java.util.ArrayList;

public class Inventory {
    private ArrayList<Item> items;

    // Constructor
    public Inventory() {
        // Initialize the items list
        items = new ArrayList<Item>();
    }

    // Method to add an item to the inventory
    public void addItem(Item item) {
        // Adds an item
        items.add(item);
        System.out.println(item + " has been added to Inventory.");
    }

    // Method to remove an item from the inventory
    public void removeItem(Item item) {
        // Removes an item if it exists, if it doesn't then implement proper error handling
        try {
            if (items.contains(item)) {
                items.remove(item);
                System.out.println(item + " has been removed from Inventory");
            } else {
                throw new IllegalArgumentException(item + " doesn't exist in Inventory");
            }
        } catch (IllegalArgumentException error) {
            System.out.println(error.getMessage());
        }
    }

    // Method to check if an item exists in the inventory
    public boolean hasItem(Item item) {
        // Checks if an item exists
        for (Item itm: items){
            if (item == itm){
                return true;
            }
        }
        return false;
    }

    // Method to display all items in the inventory
    public void displayItems() {
        // Displays all items
        System.out.println(items);
    }

    // Method to get the total number of items
    public int getItemCount() {
        // Gets the total number of items
        int numberOfItems = items.size();
        return numberOfItems;
    }
}