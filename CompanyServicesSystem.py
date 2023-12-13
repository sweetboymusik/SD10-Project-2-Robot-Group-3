# Creating a company services system
# Date Written: Dec 12th, 2023 - End date: Dec , 2023
# Authors: Benjamin Follett, Elliott Butt, Joseph Flores, Alexander Condon-Escott, Francisco Castillo, Zachary Hulan

# Import any required libraries
import datetime
import os

# Setting up program constants
f = open("Defaults.dat", "r")
NEXT_TRANS_NUM = int(f.readline().strip())
NEXT_DRIVER_NUM = int(f.readline().strip())
MONTHLY_STAND_FEE = float(f.readline().strip())
DAILY_RENTAL_FEE = float(f.readline().strip())
WEEKLY_RENTAL_FEE = float(f.readline().strip())
HST_RATE = float(f.readline().strip())
f.close()


# Setting up program functions
def add_employee(name):
    clear_console()

    while True:
        print(name)

        driver_number = NEXT_DRIVER_NUM

        while True:
            print()
            first_name = input("First name:                     ").title()
            first_name_strip = first_name.strip()
            if first_name_strip.replace(" ", "").isalpha() and str(first_name) != '':
                break
            else:
                print()
                print("FIRST NAME IS INVALID OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            last_name = input("Last name:                     ").title()
            last_name_strip = last_name.strip()
            if last_name_strip.replace(" ", "").isalpha() and str(last_name) != '':
                break
            else:
                print()
                print("LAST NAME IS INVALID OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            street_address = input("Street Address:                 ").title()
            if str(street_address) != '':
                break
            else:
                print()
                print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            city_address = input("City:                           ").title()
            if str(city_address) != '':
                break
            else:
                print()
                print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

        ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON",
                   "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
        while True:
            print()
            province = input("Province (XX):                  ").upper()
            print()
            if province == "":
                print("PROVINCE CANNOT BE BLANK. PLEASE TRY AGAIN.")
            elif len(province) != 2:
                print("INVALID INPUT. PLEASE TRY AGAIN.")
            elif province not in ProvLst:
                print("INVALID PROVINCE. PLEASE TRY AGAIN.")
            else:
                break

        while True:
            postal_code = input("Postal code (A1A1A1):           ").upper()
            if len(postal_code) != 6:
                print()
                print("POSTAL CODE IS INVALID OR CANNOT BE BLANK. PLEASE TRY AGAIN.")
                print()
                continue
            post_num = postal_code[1] + postal_code[3] + postal_code[5]
            post_let = postal_code[0] + postal_code[2] + postal_code[4]
            if post_num.isdigit() and post_let.isalpha():
                break
            else:
                print()
                print("POSTAL CODE IS INVALID. PLEASE TRY AGAIN.")
                print()

        while True:
            print()
            phone_number = input("Enter phone number (10-digits): ")
            phone_number_set = phone_number.replace(
                "-", "").replace(" ", "").replace("(", "").replace(")", "")
            if phone_number_set.isnumeric() and len(phone_number_set) == 10:
                break
            else:
                print()
                print("PHONE NUMBER IS INVALID OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            drivers_license = input(
                "Driver's License Number:                   ").upper()
            if str(drivers_license) != '':
                break
            else:
                print()
                print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            try:
                license_expiry = input(
                    "License expiry date (YYYY-MM-DD):           ")
                datetime.datetime.strptime(license_expiry, "%Y-%m-%d")
            except:
                print()
                print("INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")
            else:
                break

        while True:
            print()
            policy_company = input(
                "Insurance policy company:                   ").title()
            if str(policy_company) != '':
                break
            else:
                print()
                print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            policy_number = input(
                "Insurance policy number:                   ").upper()
            if str(policy_number) != '':
                break
            else:
                print()
                print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            own_car = input(
                "Do you own a car (Y/N):                   ").upper()
            if own_car == 'Y' or own_car == 'N':
                break
            else:
                print()
                print("INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

        balance_due = 0

        print(f"Name: {first_name} {last_name}")
        print(f"Driver Number: {driver_number}")
        print(
            f"Address: {street_address}, {city_address}, {province} {postal_code}")
        print(f"Phone Number: {phone_number}")
        print(f"License Number: {drivers_license}")
        print(f"License Expiry: {license_expiry}")
        print(f"Policy Company: {policy_company}")
        print(f"Policy Number: {policy_number}")
        print(f"Car Type: {own_car}")
        print(f"Balance Due: {balance_due}")

        f = open("Employees.dat", "a")
        f.write(f"{first_name}, {last_name}, ")
        f.write(f"{driver_number}, ")
        f.write(f"{street_address}, {city_address}, {province}, {postal_code}, ")
        f.write(f"{phone_number}, ")
        f.write(f"{drivers_license}, ")
        f.write(f"{license_expiry}, ")
        f.write(f"{policy_company}, ")
        f.write(f"{policy_number}, ")
        f.write(f"{own_car}, ")
        f.write(f"{balance_due}\n")
        f.close()

        another = input("Enter another employee? (Y/N): ").upper()
        clear_console

        if another == "N":
            clear_console
            break


def gen_report(name):
    clear_console()

    print(name)
    print()

    print("HAB TAXI SERVICES")
    print("EMPLOYEE LISTING")
    print()
    print(f"DRIVER  NAME               ADDRESS          PHONE NUMBER   LICENSE / EXPIRY     POLICY / NUMBER   OWN CAR   BALANCE")
    print("-"*115)
    f = open("Employees.dat", "r")

    emp_cnt = 0
    bal_acm = 0

    for line in f:
        line_split = line.split(", ")
        first_name = line_split[0].strip()
        last_name = line_split[1].strip()
        name = f"{first_name} {last_name}"
        driver_number = line_split[2].strip()
        city_address = line_split[4].strip()
        province = line_split[5].strip()
        address_display = f"{city_address}, {province}"
        phone_number = line_split[7].strip()
        drivers_license = line_split[8].strip()
        license_expiry = line_split[9].strip()
        policy_company = line_split[10].strip()
        policy_number = line_split[11].strip()
        own_car = line_split[12].strip()
        balance_due = float(line_split[13].strip())
        balance_display = f"${balance_due:,.2f}"

        emp_cnt += 1
        bal_acm += balance_due

        print(f"{driver_number}    {name:<18s} {address_display:<16s} {phone_number}   {drivers_license} / {license_expiry}   {policy_company:<8s} / {policy_number}    {own_car}    {balance_display:>9s}")

    bal_acm_display = f"${bal_acm:,.2f}"

    print("-"*115)
    print(
        f"NUMBER OF EMPLOYEES: {emp_cnt:02d}                                                                TOTAL BALANCE DUE: {bal_acm_display:>9s}")
    print(" "*106 + "=========")
    print()
    input("Press enter to return to the main menu...")
    clear_console()


def todo(name):
    clear_console()
    print(name)
    print()
    input("This option has not yet been implemented. Press enter to return to the main menu...")
    clear_console()


def clear_console():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


# Start of the main program.
while True:
    clear_console()

    print(f"HAB Taxi Services")
    print(f"Company Services System")
    print()
    print(f"1. Enter New Employee (driver).")
    print(f"2. Enter Company Revenues.")
    print(f"3. Enter Company Expenses.")
    print(f"4. Track Car Rentals.")
    print(f"5. Record Employee Payment.")
    print(f"6. Print Company Profit Listing.")
    print(f"7. Print Driver Financial Listing.")
    print(f"8. Print Employee Listing.")
    print(f"9. Quit Program.")
    print()

    try:
        choice = int(input("Enter choice (1-9): "))
    except:
        print("Invalid selection - must choose an option between 1-9. Please re-enter.")
    else:
        if choice <= 9 and choice >= 1:
            if choice == 1:
                add_employee("1. Enter New Employee (driver)")
                NEXT_DRIVER_NUM += 1
            if choice == 2:
                todo("2. Enter Company Revenues")
            if choice == 3:
                todo("3. Enter Company Expenses")
            if choice == 4:
                todo("4. Track Car Rentals")
            if choice == 5:
                todo("5. Record Employee Payment")
            if choice == 6:
                todo("6. Print Company Profit Listing")
            if choice == 7:
                todo("7. Print Driver Financial Listing")
            if choice == 8:
                gen_report("8. Print Employee Listing")
            if choice == 9:
                print("Thank you for using our program. Have a great day!")
                break
        else:
            print(
                "Invalid selection - must choose an option between 1-9. Please re-enter.")

# Write constants back to defaults file
f = open("Defaults.dat", "w")
f.write(f"{NEXT_TRANS_NUM}\n")
f.write(f"{NEXT_DRIVER_NUM}\n")
f.write(f"{MONTHLY_STAND_FEE}\n")
f.write(f"{DAILY_RENTAL_FEE}\n")
f.write(f"{WEEKLY_RENTAL_FEE}\n")
f.write(f"{HST_RATE}")
f.close()
