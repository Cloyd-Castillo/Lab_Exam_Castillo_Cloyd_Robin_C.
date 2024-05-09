game_library = {
    1: {"Donkey Kong": {"stocks": 3, "cost": 2, "rented": 0}},
    2: {"Super Mario Bros": {"stocks": 5, "cost": 3, "rented": 0}},
    3: {"Tetris": {"stocks": 2, "cost": 1, "rented": 0}}
}

user_accounts = {}

def admin_login():
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "adminpass":
        print("\nADMIN LOGIN SUCCESSFUL! \n")
        admin_menu()
    else:
        print("Please put the correct information")

def admin_menu():
    print("Choose the game you want to update")
    print("1. Update game details")
    print("2. Logout")

    choice = input("Enter your choice: ")

    while True:
        if choice == "1":
            update_game_details()
        elif choice == "2":
            print("Logging Out")
            main()

def update_game_details():
    print("UPDATE GAME DETAILS HERE")
    display_available_games()

    game_id = input("Enter the ID of the game you want to update: ")

    try:
        game_id = int(game_id)
        if game_id in game_library:
            print("1. Update stock")
            print("2. Update Price")
#int(price)
            choice = input("Enter your choice: ")

            if choice == "1":
                new_stock = int(input("New stock: "))
                game_name = list(game_library[game_id].keys())[0]
                game_library[game_id][game_name]["stocks"] = new_stock
                print(f"Updated {game_name}'s stock to {new_stock}")
                admin_menu()
            
            elif choice == "2":
                new_price = int(input("New price: $"))
                game_name = list(game_library[game_id].keys())[0]
                game_library[game_id][game_name]["cost"] = new_price
                print(f"Updated {game_name}'s price to {new_price}")
                admin_menu()
            
            else:
                print("Please put a valid option")
        else:
            print("Invalid game ID")
    except ValueError:
        print("Pllease enter the valid ID of the games")

def display_available_games():
    print("\n AVAILABLE GAMES:")
    for i, game in game_library.items():
        game_name = list(game.keys())[0]
        stocks = game[game_name]["stocks"]
        cost = game[game_name]["cost"]
        print(f"{i}. {game_name} - Stocks: {stocks}, Cost: ${cost}")

def register_user():
    print("\nREGISTER PAGE")
    username = input("Enter username: ")
    if username in user_accounts:
        print("This username already exists. Try another name.")
        return

    while True:
        password = input("Enter password: ")
        if len(password) >= 8:
            print("ACCOUNT REGISTERED SUCCESSFULLY!")
            user_accounts[username] = {
                "username": username,
                "password": password,
                "inventory": {},
                "balance": 0,
                "points": 0,
                "activities": []
            }
            break
        else:
            print("Password must be at least 8 characters long. Please try again.")

def check_credentials(username, password):
    if username in user_accounts:
        if user_accounts[username]["password"] == password:
            print("Login successful!")
            logged_in_menu(username)
            return True
    print("Invalid username or password.")
    return False

def log_in():
    print("\nLOG IN PAGE")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return check_credentials(username, password)


def logged_in_menu(username):
    print("\n Menu")
    print("1. Rent game")
    print("2. Return game")
    print("3. Top-up")
    print("4. Check points")
    print("5. Redeem free rental")
    print("6. Display Inventory")
    print("7. Logout and see Receipt")

    choice = input("Enter your choice: ")

    while True:
        if choice == "1":
            rent_game(username)
        elif choice == "2":
            return_game(username)
        elif choice == "3":
            top_up_account(username)
        elif choice == "4":
            check_points(username)
        elif choice =="5":
            redeem_free_rental(username)
        elif choice == "6":
            display_inventory(username)
        elif choice == "7":
            receipt(username)
            print("Logging out...")
            main()
        else:
            print("Please choose a valid option.")

def rent_game(username):
    display_available_games()
    choice = input("Select the game you want to rent: ")
    try:
        choice = int(choice)
        if choice in game_library:
            game_name = list(game_library[choice].keys())[0]
            if game_library[choice][game_name]["stocks"] > 0:
                if user_accounts[username]["balance"] >= game_library[choice][game_name]["cost"]:
                    user_accounts[username]["balance"] -= game_library[choice][game_name]["cost"]
                    game_library[choice][game_name]["stocks"] -= 1
                    game_library[choice][game_name]["rented"] += 1

                    user_accounts[username]["inventory"][game_name] = user_accounts[username]["inventory"].get(game_name, 0) + 1
                    
                    user_accounts[username]["activities"].append(f"Rented {game_name}. Balance: ${user_accounts[username]['balance']}")

                    print(f"{game_name} rented successfully. Balance now: ${user_accounts[username]['balance']}")

                    logged_in_menu(username)
                else:
                    print("You do not have enough balance. Please top up your account.")
                    logged_in_menu(username)
            else:
                print("There's no available stock for this game right now")
                logged_in_menu(username)
        else:
            print("Please put a valid option")
    except ValueError:
        print("Please enter a valid number")

def return_game(username):
    print("\nRETURN GAME")
    if user_accounts[username]["inventory"]:
        for game_name, quantity in user_accounts[username]["inventory"].items():
            print(f"{game_name}: {quantity} copies")
        game_name = input("Enter the game name you want to return: ")
        if game_name in user_accounts[username]["inventory"] and user_accounts[username]["inventory"][game_name] > 0:
            user_accounts[username]["inventory"][game_name] -= 1
            if user_accounts[username]["inventory"][game_name] == 0:
                del user_accounts[username]["inventory"][game_name]
            for game_id, details in game_library.items():
                if game_name in details:
                    game_library[game_id][game_name]["stocks"] += 1
                    game_library[game_id][game_name]["rented"] -= 1

                    cost_of_returned_game = game_library[game_id][game_name]["cost"]
                    points_earned = float(cost_of_returned_game * 0.5) 
                    user_accounts[username]["points"] += points_earned

                    user_accounts[username]["activities"].append(f"Returned {game_name}. Earned {points_earned} points.")

                    print(f"Returned {game_name} successfully. Earned {points_earned} points.")
                    logged_in_menu(username)
            else:
                print("You did not rent this game or input is incorrect.")
    else:
        print("You have no rented games to return.")

def redeem_free_rental(username):
    if user_accounts[username]["points"] >= 3: #mali
        display_available_games()
        game_choice = input("Select a game for free rental (enter number): ")
        try:
            game_choice = int(game_choice)
            if game_choice in game_library:
                game_name = list(game_library[game_choice].keys())[0]
                if game_library[game_choice][game_name]["stocks"] > 0:
                    user_accounts[username]["points"] -= 3
                    game_library[game_choice][game_name]["stocks"] -= 1
                    game_library[game_choice][game_name]["rented"] += 1
                    user_accounts[username]["inventory"][game_name] = user_accounts[username]["inventory"].get(game_name, 0) + 1
                    user_accounts[username]["activities"].append(f"Redeemed free rental for {game_name}. Deducted 3 points.")
                    print(f"Successfully redeemed {game_name} for free. Remaining points: {user_accounts[username]['points']}")
                    logged_in_menu(username)
                else:
                    print("Sorry, no copies available for renting.")
                    logged_in_menu(username)
            else:
                print("Invalid game choice.")
                logged_in_menu(username)
        except ValueError:
            print("Please enter a valid number")
    else:
        print("Insufficient points for free rental. You need at least 3 points.")
        logged_in_menu(username)


def top_up_account(username):
    try:
        amount = float(input("Enter amount to top-up: "))
        user_accounts[username]["balance"] += amount

        user_accounts[username]["activities"].append(f"Topped up ${amount}. New balance: ${user_accounts[username]['balance']}")

        print(f"Balance updated. New balance is: ${user_accounts[username]['balance']}")

        logged_in_menu(username) #para bumalik
    except ValueError:
        print("Please enter a valid number.")
    
def check_points(username):
    print(f"Your current points: {user_accounts[username]['points']}")
    logged_in_menu(username)
    
def display_inventory(username):
    print("YOUR INVENTORY:")
    inventory = user_accounts[username]["inventory"]
    if inventory:
        for game_name, quantity in inventory.items():
            print(f"{game_name}: {quantity}")
            logged_in_menu(username)
    else:
        print("Your inventory is empty.")
        logged_in_menu(username)

def receipt(username):
    print("\n--- Receipt ---")
    if "activities" in user_accounts[username] and user_accounts[username]["activities"]:
        for activity in user_accounts[username]["activities"]:
            print(activity)
    else:
        print("No activities recorded.")
    print(f"Final Balance: ${user_accounts[username]['balance']}") #sheesh

def main():
    while True:
        print("\n GAME RENTAL SYSTEM")
        print("1. Display available games")#111
        print("2. Register")
        print("3. Log in")
        print("4. Admin Log in")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_available_games()
        elif choice == "2":
            register_user()
        elif choice == "3":
            log_in()
        elif choice == "4":
            admin_login()
        elif choice == "5":
            print("Closing code...")
            break
        else:
            print("Please put a valid option")

if __name__ == "__main__":
    main()

