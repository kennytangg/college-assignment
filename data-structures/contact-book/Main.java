import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        boolean running = true;
        Scanner scanner = new Scanner(System.in);
        ContactBook contactBook = new ContactBook();

        while (running){
            // print menu every loop
            String input = contactBook.printMenu();
            switch (input.toUpperCase()){
                // Add Contact
                case "A":
                    System.out.print("\nWrite Contact Name: ");
                    String name = scanner.next();

                    System.out.print("Write Contact Phone Number: ");
                    String phoneNumber = scanner.next();

                    System.out.print("Write Contact Email: ");
                    String email = scanner.next();

                    contactBook.addContact(name, phoneNumber, email);
                    break;
                    
                // Delete Contact    
                case "D":
                    System.out.print("\nDelete Contact Name: ");
                    String delName = scanner.next();
                    contactBook.deleteContact(delName);
                    break;
                    
                // Email Search
                case "E":
                    System.out.print("\nWrite Contact Email: ");
                    String contactEmail = scanner.next();
                    contactBook.emailSearch(contactEmail);
                    break;
                    
                // Print Contact Book List
                case "P":
                    contactBook.printList();
                    break;
                    
                // Name Search
                case "N":
                    System.out.print("\nWrite Contact Name: ");
                    String contactName = scanner.next();
                    contactBook.nameSearch(contactName);
                    break;
                    
                // Phone Number Search
                case "S":
                    System.out.print("\nWrite Contact Phone Number: ");
                    String phoneNum = scanner.next();
                    contactBook.numSearch(phoneNum);
                    break;
                    
                // Quit and break the loop
                case "Q":
                    System.out.println("Bye !");
                    running = false;
                    break;

                default:
                    System.out.println("Unknown Entry");
            }
        }
    }
}
