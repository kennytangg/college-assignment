public class Contact {
    private String name;
    private String phoneNumber;
    private String email;
    public Contact next;
    public Contact prev;

    // Constructor
    public Contact(String name, String phoneNumber, String email) {
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.email = email;
        this.next = null;
        this.prev = null;
    }

    // method to get name
    public String getName(){
        return this.name;
    }

    // method to get phone number
    public String getPhoneNumber(){
        return this.phoneNumber;
    }

    // method to get email
    public String getEmail(){
        return this.email;
    }

    @Override
    public String toString(){
        return "Name: " + this.name +", Phone Number: " + this.phoneNumber + ", Email: " + this.email;
    }
}