public class BankAppDriver {
    // Main method to run the program
    public static void main(String[] args) {
        // Create a BankAccount object
        BankAccount normalAccount = new BankAccount(501, "John Doe", 5000.0);
        System.out.println("Bank Account Details:");
        normalAccount.check_balance();
        normalAccount.deposit_money(1500.0);
        normalAccount.withdraw_money(2000.0);
        normalAccount.check_balance();

        // Create a SavingsAccount object
        SavingsAccount savingsAccount = new SavingsAccount(502, "Kaine Smith", 10000.0, 5);
        System.out.println("\nSavings Account Details:");
        savingsAccount.check_balance();
        savingsAccount.deposit_money(2000.0);
        savingsAccount.apply_interest();
        savingsAccount.withdraw_money(3000.0);
        savingsAccount.check_balance();
    }

}
