public class SavingsAccount extends BankAccount {
    // Attributes for subclass SavingsAccount
    private int interest_rate;

    // Constructor for subclass SavingsAccount
    public SavingsAccount(int account_number, String account_holder_name, double balance, int interest_rate) {
        super(account_number, account_holder_name, balance);
        this.interest_rate = interest_rate;
    }

    // Method to apply interest
    public void apply_interest() {
        double interestAmount = balance * (interest_rate / 100.0);
        balance += interestAmount;
        System.out.println("Applied interest: " + interestAmount + ". New Balance: " + balance);
    }

    // Main method to run the program
    public static void main(String[] args) {
        // Create a SavingsAccount object
        SavingsAccount savingsAccount = new SavingsAccount(502, "Kaine Smith", 10000.0, 5);
        System.out.println("\nSavings Account Details:");
        savingsAccount.check_balance();
        savingsAccount.apply_interest();
        savingsAccount.check_balance();
    }
}
