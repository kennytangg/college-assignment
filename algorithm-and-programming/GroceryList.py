choice = 0
grocery_list = []
while choice != 4:
    print("\nChoose an Option")
    print("[1] Add an Item ")
    print("[2] View the list ")
    print("[3] Remove an item")
    print("[4] Exit ")
    choice = int(input("Enter your Choice: "))
    match choice:
        case 1: 
            item = input("Enter the item to add: ")
            grocery_list.append(item)
            print(f"Item {item} added to the grocery list.")
        case 2:
           count = 0
           for list in grocery_list:
               count += 1
               print(f"{count}. {list}")
        case 3:
            delete = input("Enter item to Remove: ")
            if delete in grocery_list:
                grocery_list.remove(delete)
                print("the item {delete} has been remove.")
            else:
                print("The item is not in the grocery list.")
        case 4:
            print("See you next Time")
            break
        case _:
            print("Not a Valid Command")
