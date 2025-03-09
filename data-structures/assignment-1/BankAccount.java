public class BankAccount {
    // Attributes for class BankAccount
    protected int account_number;
    protected String account_holder_name;
    protected double balance;

    // Constructor for class BankAccount 
    public BankAccount(int account_number, String account_holder_name, double balance) {
        this.account_number = account_number;
        this.account_holder_name = account_holder_name;
        this.balance = balance;
    }

    // Method for Depositing Money
    public void deposit_money(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount + ". New Balance: " + balance);
    }

    // Method for Withdrawing Money
    public void withdraw_money(double amount) {
        if (balance < amount) {
            System.out.println("Not enough money to withdraw " + amount);
        } else {
            balance -= amount;
            System.out.println("Withdrew: " + amount + ". New Balance: " + balance);
        }
    }

    // Method for Checking Balance
    public void check_balance() {
        System.out.println("Current Balance: " + balance);
    }

    // Main method to run the program
    public static void main(String[] args) {
        BankAccount account = new BankAccount(501, "John Doe", 5000.0);
        System.out.println("Bank Account Details:");
        account.check_balance();
        account.deposit_money(1500.0);
        account.withdraw_money(2000.0);
        account.check_balance();
    }
}
