import json
import os
import datetime

DATABASE = "bank_db.json"


# -------------------- DATABASE HANDLING --------------------
def load_db():
    if not os.path.exists(DATABASE):
        with open(DATABASE, "w") as f:
            json.dump({"users": {}}, f)

    with open(DATABASE, "r") as f:
        return json.load(f)


def save_db(db):
    with open(DATABASE, "w") as f:
        json.dump(db, f, indent=4)



# -------------------- ACCOUNT OPERATIONS --------------------
def create_account():
    db = load_db()

    print("\n=== CREATE NEW ACCOUNT ===")
    username = input("Choose username: ")

    if username in db["users"]:
        print("❌ Username already exists.")
        return

    password = input("Choose password: ")
    acc_no = str(100000 + len(db["users"]))

    db["users"][username] = {
        "password": password,
        "account_no": acc_no,
        "balance": 0,
        "history": []
    }

    save_db(db)

    print(f"✔ Account created successfully! Your account number: {acc_no}")


def login():
    db = load_db()
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in db["users"] and db["users"][username]["password"] == password:
        print("✔ Login successful!")
        return username

    print("❌ Invalid login.")
    return None



# -------------------- BANKING FEATURES --------------------
def deposit(user):
    db = load_db()
    amount = float(input("Enter amount to deposit: "))

    db["users"][user]["balance"] += amount
    db["users"][user]["history"].append(
        f"{timestamp()} | Deposited: {amount}"
    )

    save_db(db)
    print("✔ Deposit successful!")


def withdraw(user):
    db = load_db()
    amount = float(input("Enter amount to withdraw: "))

    if amount > db["users"][user]["balance"]:
        print("❌ Insufficient funds.")
        return

    db["users"][user]["balance"] -= amount
    db["users"][user]["history"].append(
        f"{timestamp()} | Withdrawn: {amount}"
    )

    save_db(db)
    print("✔ Withdrawal successful!")


def transfer(user):
    db = load_db()

    target = input("Enter receiver username: ")
    amount = float(input("Enter amount to transfer: "))

    if target not in db["users"]:
        print("❌ Target user does not exist.")
        return

    if amount > db["users"][user]["balance"]:
        print("❌ Insufficient balance.")
        return

    db["users"][user]["balance"] -= amount
    db["users"][target]["balance"] += amount

    db["users"][user]["history"].append(
        f"{timestamp()} | Sent {amount} to {target}"
    )
    db["users"][target]["history"].append(
        f"{timestamp()} | Received {amount} from {user}"
    )

    save_db(db)
    print("✔ Transfer successful!")


def show_balance(user):
    db = load_db()
    balance = db["users"][user]["balance"]
    print(f"\n💰 Current Balance: {balance}")


def show_history(user):
    db = load_db()
    print("\n=== TRANSACTION HISTORY ===")
    for h in db["users"][user]["history"]:
        print(h)



# -------------------- UTIL --------------------
def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



# -------------------- MAIN MENU --------------------
def main_menu(user):
    while True:
        print("\n===== BANKING MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Balance")
        print("5. Transaction History")
        print("6. Logout")

        choice = input("Choose: ")

        if choice == "1":
            deposit(user)
        elif choice == "2":
            withdraw(user)
        elif choice == "3":
            transfer(user)
        elif choice == "4":
            show_balance(user)
        elif choice == "5":
            show_history(user)
        elif choice == "6":
            print("✔ Logged out.")
            break
        else:
            print("Invalid choice.")



# -------------------- APP START --------------------
def main():
    while True:
        print("\n====== PYTHON BANKING APP ======")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        option = input("Choose: ")

        if option == "1":
            create_account()
        elif option == "2":
            user = login()
            if user:
                main_menu(user)
        elif option == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
