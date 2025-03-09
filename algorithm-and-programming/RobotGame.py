import random

def move_to_zone(choice): # move zones
     while True: #error handling
        try:
            return int(input(choice))
        except ValueError:
            print("Invalid Choice!\n") #if error print this

def collect_item(item): #add item to inventory
    if item not in inventory: # if item is not in inventory
        inventory.append(item) #add the item to the Inventory list
    else:
        print(f"You already have {item} in the inventory.")

def display_inventory():
    print(inventory) #display inventory

def map(): # function to make a 64 of zeros
    return [[0  for i in range(8)] for i in range(8)] 

def map_print(map):
    for i in map:
        print(" ".join(str(j) for j in i)) 
        #print the 0 from the nested loop and make the map into 8x8
    print()

def random_one_and_item(map:list):
    a = random.randint(0, 7)
    b = random.randint(0, 7)
    x = random.randint(0, 7)
    y = random.randint(0, 7)

    while (a,b) == (x,y):
        x, y = random.randint(0, 7), random.randint(0, 7)

    map[a][b] = 1
    map[x][y] = "X"

    return (a,b),(x,y)

def move_one(map, current_pos, direction):
    global count,battery_level #global variable

    x, y = current_pos # current position in (x,y)
    count += 1

    if count == 5:
        battery_level -= 5
        count = 0

    if direction.upper() == 'W' and x > 0:       # Move Up
        new_pos = (x - 1, y)
    elif direction.upper() == 'S' and x < 7:     # Move Down
        new_pos = (x + 1, y)
    elif direction.upper() == 'A' and y > 0:     # Move Left
        new_pos = (x, y - 1)
    elif direction.upper() == 'D' and y < 7:     # Move Right
        new_pos = (x, y + 1)
    else:
        return current_pos  # dont move
    
    #Update map
    map[x][y] = 0  # make the previous "0"
    map[new_pos[0]][new_pos[1]] = 1  # Set new position to "1"

    return new_pos  # Return the new position

def main():
    global battery_level,option
    while True:
        if inventory == ["PowerCell 1","PowerCell 2","PowerCell 3"]:
            break
        if battery_level <= 0:
            break

        print("\n=== Welcome to Robot Explorer Game ===\n")
        print('''Pick a Zone to Explore !
1) Zone X
2) Zone Y
3) Zone Z
4) Zone A
5) Zone B
6) Zone C
7) Inventory Check
8) Quit
        ''')
        option = move_to_zone("Choose an Option(1/2/3/4/5/6/7/8): ")
        if option in range (1,4):
            maps = map()
            location, items = random_one_and_item(maps)
            current_pos = location
            map_print(maps)
            while True: #loop until input is w/a/s/d
                direction = input("Move (w/a/s/d): ")
                if direction.upper() in ['W', 'A', 'S', 'D']:
                    current_pos = move_one(maps, current_pos, direction)
                    print(f"\nBattery Level: {battery_level}%")
                    map_print(maps)
                    if battery_level <= 0:
                        break
                    if current_pos == items:
                        if option in range(2,5):
                            rand = random.randint(0,1)
                        else:
                            rand = random.randint(0,2)
                        values = zones_in_the_city[option]
                        item = values[rand]
                        if item == "Short Circuit":
                            battery_level -= 10
                            if battery_level > 100:
                                battery_level = 100
                            print(f"{item} collected!, Battery Level Went Down to {battery_level}%")
                            break
                        elif item == "Battery Pack":
                            battery_level += 10
                            if battery_level > 100:
                                battery_level = 100
                            print(f"{item} collected!, Battery Level Went Up to {battery_level}%")
                            break
                        else:
                            collect_item(item)
                            print(f"Battery Level: {battery_level}%")
                            print(inventory)
                            print(f"{item} collected!")
                            break  # Exit loop
                else:
                    print("Invalid input! Use w, a, s, or d.\n")
        elif option in range(4,7):
            if "PowerCell 1" not in inventory:
                print("-- This Zone will only be available if you collected PowerCell 1 --")
            else:
                maps = map()
                location, items = random_one_and_item(maps)
                current_pos = location
                map_print(maps)
                while True: #loop until input is w/a/s/d
                    direction = input("Move (w/a/s/d): ")
                    if direction.upper() in ['W', 'A', 'S', 'D']:
                        current_pos = move_one(maps, current_pos, direction)
                        print(f"\nBattery Level: {battery_level}%")
                        map_print(maps)
                        if battery_level <= 0:
                            break
                        if current_pos == items:
                            if option in range(2,5):
                                rand = random.randint(0,1)
                            else:
                                rand = random.randint(0,2)
                            values = zones_in_the_city[option]
                            item = values[rand]
                            if item == "Short Circuit X":
                                battery_level -= 20
                                if battery_level > 100:
                                    battery_level = 100
                                print(f"{item} collected!, Battery Level Went Down to {battery_level}%")
                                break
                            elif item == "Battery Pack Y":
                                battery_level += 5
                                if battery_level > 100:
                                    battery_level = 100
                                print(f"{item} collected!, Battery Level Went Up to {battery_level}%")
                                break
                            else:
                                collect_item(item)
                                print(f"Battery Level: {battery_level}%")
                                print(inventory)
                                print(f"{item} collected!")
                                break  # Exit loop
                    else:
                        print("Invalid input! Use w, a, s, or d.\n")
        elif option == 7:
            display_inventory()    
        elif option == 8:
            break # Exit loop
        else:
            print("Invalid Choice!\n")

battery_level = 100
inventory = [] 
count = 0
zones_in_the_city = {
    1:["PowerCell 1","Short Circuit","Battery Pack"],   #zone X
    2:["Short Circuit","Battery Pack"],                 #zone Y
    3:["Short Circuit","Battery Pack"],                 #zone Z
    4:["Short Circuit X","Battery Pack Y"],                 #zone A
    5:["PowerCell 2","Short Circuit X","Battery Pack Y"],   #zone B
    6:["PowerCell 3","Short Circuit X","Battery Pack Y"],   #zone C
    }

main()

if battery_level > 0 and len(inventory) == 3:
    print("\n== Congratulation ! You Have Collected All Power Cells ==")
elif battery_level <= 0:
    print("You Lose ! Your battery level have reach 0")
elif option == 8:
    print("See You Next Time")