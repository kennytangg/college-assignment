public class InventoryDriver {
    public static void main(String args[]) {
        String itm;
        boolean hasItem;
        int itemCount;

        Item item1 = new Item("Laptop");
        Item item2 = new Item("Phone");
        Item item3 = new Item("Bag");
        Item item4 = new Item("Watch");

        itm = item3.getName();
        System.out.println(itm);

        Inventory invent = new Inventory();
        invent.addItem(item1);
        invent.addItem(item2);
        invent.addItem(item3);
        invent.addItem(item4);

        itemCount = invent.getItemCount();
        System.out.println(itemCount);

        invent.displayItems();

        hasItem = invent.hasItem(item1);
        System.out.println(hasItem);

        invent.removeItem(item1);
        invent.displayItems();
        invent.removeItem(item1);
    }
}
