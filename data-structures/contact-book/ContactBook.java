import java.util.*;

public class ContactBook {
    Contact head = null;
    Contact tail = null;
    public static Scanner scanner = new Scanner(System.in);

    // Constructor
    public ContactBook(){
        this.head = null;
        this.tail = null;
    }

    // Print Contact Book Menu
    public String printMenu() {
        System.out.println("\n=== Welcome to ContactBook ===");
        System.out.println("Menu :");
        System.out.println("(A)dd");
        System.out.println("(D)elete");
        System.out.println("(E)mail Search");
        System.out.println("(P)rint List");
        System.out.println("(N)ame Search");
        System.out.println("(S)earch Phone Number");
        System.out.println("(Q)uit");
        System.out.println("==============================");
        System.out.print("Enter a Command : ");
        return scanner.next();
    }

    // method to add contact to contact book
    public void addContact(String name, String phoneNumber,String email){
        Contact newContact = new Contact(name, phoneNumber, email);

        // doesn't add new contact if same contact already in contact book
        boolean isContain = contain(name,phoneNumber,email);
        if (isContain){
            System.out.println(newContact.getName() + " is already in contact book");
            return;
        }

        // if list is empty
        if (this.head == null){
            this.head = newContact;
            this.tail = newContact;
        } else{
            this.tail.next = newContact;
            newContact.prev = this.tail;
            this.tail = newContact;
        }
        System.out.println("\n" + newContact.getName() + " has been added to the Contact Book");
    }

    // method to delete contact
    public void deleteContact(String name) {
        if (head == null) {
            System.out.println("There are no contacts to delete");
            return;
        }
        Contact current = this.head;
        while (!current.getName().equalsIgnoreCase(name)){
            current = current.next;
            if (current == null){
                System.out.println("Contact not found");
                return;
            }
        }

        // if the list only has one contact
        if (head == tail) {
            head = null;
            tail = null;
        }

        // if the removed contact is the first element
        else if (current.prev == null) {
            head = current.next;
            current.next.prev = null;
        }

        // if the removed contact is the last element
        else if (current.next == null){
            tail = current.prev;
            current.prev.next = null;
        } else {
            current.prev.next = current.next;
            current.next.prev = current.prev;
        }
        System.out.println(name + " has been removed");
    }

    // method to print the list in  contact book
    public void printList(){
        Contact current = head;
        if (current == null){
            System.out.println("Contact Book is empty");
            return;
        }
        System.out.println("\n Contact Book : ");
        // print all contact in contact book
        while(current != null) {
            System.out.println(current);
            current = current.next;
        }
    }

    // method to search contact using email
    public void emailSearch(String email){
        // if list is empty
        if (head == null) {
            System.out.println("The contact book is empty");
            return;
        }

        Contact current = this.head;
        while (!current.getEmail().equalsIgnoreCase(email)){
            current = current.next;
            if (current == null){
                System.out.println("Email not found");
                return;
            }
        }
        System.out.println(current);
    }

    // method to search contact using name
    public void nameSearch(String name){
        // if list is empty
        if (head == null) {
            System.out.println("The contact book is empty");
            return;
        }
        Contact current = this.head;
        while (!current.getName().equalsIgnoreCase(name)){
            current = current.next;
            if (current == null){
                System.out.println("Name not found");
                return;
            }
        }
        System.out.println(current);
    }

    // method to search contact using Phone Number
    public void numSearch(String num){
        // if list is empty
        if (head == null) {
            System.out.println("The contact book is empty");
            return;
        }
        Contact current = this.head;
        while (!current.getPhoneNumber().equals(num)){
            current = current.next;
            if (current == null){
                System.out.println("Phone Number not found");
                return;
            }
        }
        System.out.println(current);
    }

    // method to check if the contact has already exists
    public boolean contain(String name, String num, String email){
        Contact current = head;
        while (current != null){
            if (current.getName().equalsIgnoreCase(name) &&
                current.getPhoneNumber().equals(num) &&
                current.getEmail().equalsIgnoreCase(email)){
                return true;
            }
            current = current.next;
        }
        return false;
    }
}
