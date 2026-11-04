
# Blood Bank Management System
# Project Number: 78

BLOOD_GROUPS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

blood_stock = {
    "A+": 10,
    "A-": 0,
    "B+": 5,
    "B-": 0,
    "AB+": 2,
    "AB-": 0,
    "O+": 8,
    "O-": 0
}

DONOR_FILE = "donors.txt"


# Create donor file if it does not exist
def create_donor_file():
    with open(DONOR_FILE, "a", encoding="utf-8"):
        pass


# Test Case 1: Add Donor
def add_donor():
    name = input("Enter donor name: ").strip()

    if not name:
        print("Donor name cannot be empty.")
        return

    group = input("Enter blood group: ").strip().upper()

    if group not in BLOOD_GROUPS:
        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    try:
        units = int(input("Enter number of units donated: "))
        if units <= 0:
            print("Units must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number of units.")
        return

    blood_stock[group] += units

    with open(DONOR_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name}|{group}|{units}\n")

    print(
        f"Donor saved to donors.txt. "
        f"Stock of {group} is now {blood_stock[group]} units."
    )


# Test Case 2: Issue Blood
def issue_blood():
    group = input("Enter blood group required: ").strip().upper()

    if group not in BLOOD_GROUPS:
        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    try:
        units = int(input("Enter number of units required: "))
        if units <= 0:
            print("Units must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number of units.")
        return

    if blood_stock[group] < units:
        print(
            f"Insufficient stock: only {blood_stock[group]} "
            f"unit(s) of {group} available."
        )
        return

    blood_stock[group] -= units

    print(
        f"{units} unit(s) of {group} issued. "
        f"Stock of {group} is now {blood_stock[group]} units."
    )


# Test Case 3: View Blood Stock
def view_stock():
    print("\n===== Available Blood Stock =====")

    for group in BLOOD_GROUPS:
        print(f"{group}: {blood_stock[group]} unit(s)")

    print("=================================")


# Test Case 4: Search Donors
def search_donors():
    group = input("Enter blood group to search: ").strip().upper()

    if group not in BLOOD_GROUPS:
        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    create_donor_file()
    found = []

    with open(DONOR_FILE, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("|")

            if len(parts) != 3:
                continue

            name, donor_group, units = parts

            if donor_group.strip().upper() == group:
                found.append((name.strip(), units.strip()))

    if not found:
        print(f"No donors found with blood group {group}.")
        return

    print(f"Donors with blood group {group}:")

    for number, (name, units) in enumerate(found, start=1):
        print(f"{number}. {name} - {units} unit(s)")

    print(f"Total donors found: {len(found)}")


# Test Case 5: Exit Program
def exit_program():
    print("Thank you for using the Blood Bank Management System.")


# Main Menu
def main():
    create_donor_file()

    while True:
        print("\n===== Blood Bank Management System =====")
        print("1. Add donor")
        print("2. Issue blood")
        print("3. View stock")
        print("4. Search donors")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_donor()

        elif choice == "2":
            issue_blood()

        elif choice == "3":
            view_stock()

        elif choice == "4":
            search_donors()

        elif choice == "5":
            exit_program()
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
