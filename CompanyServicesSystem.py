# Creating a company services system
# For HAB Taxi Services
# Dates Written: Dec 12th, 2023 - Dec 15, 2023
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
TODAY = datetime.datetime.today()
f.close()


# Setting up program functions
def add_employee(name):
    clear_console()

    while True:
        print(name)

        driver_number = NEXT_DRIVER_NUM

        while True:
            print()
            first_name = input(
                "First name: ").title()
            first_name_strip = first_name.strip()
            if first_name_strip.replace(" ", "").isalpha() and str(first_name) != '':
                break
            else:
                print()
                print("FIRST NAME IS INVALID OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            last_name = input("Last name: ").title()
            last_name_strip = last_name.strip()
            if last_name_strip.replace(" ", "").isalpha() and str(last_name) != '':
                break
            else:
                print()
                print("LAST NAME IS INVALID OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            street_address = input("Street Address: ").title()
            if str(street_address) != '':
                break
            else:
                print()
                print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            city_address = input("City: ").title()
            if str(city_address) != '':
                break
            else:
                print()
                print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

        ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON",
                   "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
        while True:
            print()
            province = input("Province (XX): ").upper()
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
            postal_code = input("Postal code (A1A1A1): ").upper()
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
                "Driver's License Number: ").upper()
            if str(drivers_license) != '':
                break
            else:
                print()
                print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            try:
                license_expiry = input(
                    "License expiry date (YYYY-MM-DD): ")
                datetime.datetime.strptime(license_expiry, "%Y-%m-%d")
            except:
                print()
                print(
                    "INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")
            else:
                if datetime.datetime.strptime(license_expiry, "%Y-%m-%d").date() >= datetime.datetime.now().date():
                    break
                else:
                    print()
                    print(
                        "INVALID INPUT. CANNOT BE EARLIER THAN TODAY'S DATE OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            policy_company = input(
                "Insurance policy company: ").title()
            if str(policy_company) != '':
                break
            else:
                print()
                print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            policy_number = input(
                "Insurance policy number: ").upper()
            if str(policy_number) != '':
                break
            else:
                print()
                print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            print()
            own_car = input(
                "Do you own a car (Y/N): ").upper()
            if own_car == 'Y' or own_car == 'N':
                break
            else:
                print()
                print("INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

        balance_due = 0

        print()
        print("Details Entered:")
        print("----------------")
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
        print(f"Balance Due: ${balance_due:,.2f}")
        print()

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

        while True:
            print()
            another = input("Enter another employee? (Y/N): ").upper()
            if another == 'Y':
                break
            elif another == 'N':
                return
            else:
                print()
                print("INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")


def gen_employee_listing(name):
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


def gen_driver_fin_listing(name):
    while True:
        clear_console()
        print(name)
        print()

        emp_arr = []

        f = open("Employees.dat", "r")
        for line in f:
            line_split = line.split(", ")
            emp_arr.append(line_split[2].strip())
        f.close()

        while True:
            driver_num = input("Enter driver number (####): ")

            if len(driver_num) != 4:
                print()
                print("MUST BE A VALID 4-DIGIT NUMBER. PLEASE RE-ENTER.")
                print()
            elif driver_num not in emp_arr:
                print()
                print("NOT A VALID DRIVER NUMBER. PLEASE RE-ENTER.")
                print()
            else:
                break

        while True:
            try:
                print()
                start_date = input(
                    "Enter start date (YYYY-MM-DD): ")
                datetime.datetime.strptime(start_date, "%Y-%m-%d")
            except:
                print()
                print(
                    "INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")
            else:
                if datetime.datetime.strptime(start_date, "%Y-%m-%d").date() <= datetime.datetime.now().date():
                    break
                else:
                    print()
                    print(
                        "INVALID INPUT. CANNOT BE LATER THAN TODAY'S DATE OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

        while True:
            try:
                print()
                end_date = input(
                    "Enter end date (YYYY-MM-DD): ")
                datetime.datetime.strptime(end_date, "%Y-%m-%d")
            except:
                print()
                print(
                    "INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")
            else:
                if (datetime.datetime.strptime(end_date, "%Y-%m-%d").date() >= datetime.datetime.strptime(start_date, "%Y-%m-%d").date()) and (datetime.datetime.strptime(end_date, "%Y-%m-%d").date() <= datetime.datetime.now().date()):
                    break
                else:
                    print()
                    print(
                        "INVALID INPUT. CANNOT BE LATER THAN TODAY'S DATE OR EARLIER THAN START DATE, OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

        clear_console()

        print(name)
        print()
        print("HAB TAXI SERVICES")
        print("DRIVER FINANCIAL LISTING")
        print()
        print(f"DRIVER NUMBER: {driver_num}")
        print(f"START DATE:    {start_date}")
        print(f"END DATE:      {end_date}")
        print()
        print("=" * 65)
        print()
        print(" ID        DATE         DESC.       AMOUNT       HST       TOTAL")
        print("-" * 65)

        f = open("Revenues.dat", "r")
        trans_cnt = 0
        amt_acm = 0
        tax_acm = 0
        total_acm = 0

        for line in f:
            line_split = line.split(", ")

            if line_split[1].strip() != driver_num:
                continue

            trans_id = line_split[0].strip()
            trans_date = line_split[2].strip()
            desc = line_split[3].strip()
            amount = float(line_split[4].strip())
            taxes = float(line_split[5].strip())
            total = float(line_split[6].strip())

            if datetime.datetime.strptime(trans_date, "%Y-%m-%d").date() >= datetime.datetime.strptime(start_date, "%Y-%m-%d").date() and datetime.datetime.strptime(trans_date, "%Y-%m-%d").date() <= datetime.datetime.strptime(end_date, "%Y-%m-%d").date():
                print(
                    f" {trans_id:3s}    {trans_date:10s}   {desc:13s}{format_dollars(amount)}  {format_dollars(taxes)}  {format_dollars(total)}")

                trans_cnt += 1
                amt_acm += amount
                tax_acm += taxes
                total_acm += total

        print(" " * 34 + "-" * 31)
        print(
            f"TOTAL TRANSACTIONS: {trans_cnt:03d}   TOTALS: {format_dollars(amt_acm)}  {format_dollars(tax_acm)}  {format_dollars(total_acm)}")
        print(" " * 34 + "=" * 31)

        while True:
            print()
            another = input("Generate another report? (Y/N): ").upper()
            if another == 'Y':
                break
            elif another == 'N':
                return
            else:
                print()
                print("INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")


def add_revenue(emp, amt):
    global NEXT_TRANS_NUM

    entry_arr = []

    f = open("Revenues.dat", "a")

    entry_arr.append(f"{NEXT_TRANS_NUM}")
    entry_arr.append(emp[2])
    entry_arr.append(f"{TODAY.date()}")
    entry_arr.append("Standing Fees")
    entry_arr.append(f"{amt}")
    entry_arr.append(f"{amt * HST_RATE}")
    entry_arr.append(f"{amt + (amt * HST_RATE)}")

    f.write(f"{', '.join(entry_arr)}\n")

    NEXT_TRANS_NUM += 1


def format_dollars(amt):
    fmt1 = f"${amt:,.2f}"
    fmt2 = f"{fmt1:>9s}"

    return fmt2


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


def update_bal_revenue():
    emp_arr = []

    if TODAY.day == 1:
        f = open("Employees.dat", "r")

        for line in f:
            line_split = line.split(", ")

            if line_split[len(line_split) - 2] == "N":
                line_split[len(line_split) -
                           1] = line_split[len(line_split) - 1].strip()
                emp_arr.append(line_split)
                continue

            bal_due = float(line_split[len(line_split) - 1].strip())
            bal_due += MONTHLY_STAND_FEE + (MONTHLY_STAND_FEE * HST_RATE)

            line_split[len(line_split) - 1] = f"{bal_due}"
            emp_arr.append(line_split)

            add_revenue(line_split, MONTHLY_STAND_FEE)

        f.close()

        f = open("Employees.dat", "w")
        for line in emp_arr:
            f.write(f"{', '.join(line)}\n")
        f.close()


# 'automatically' update balance due and revenue table on first of month (see function)
update_bal_revenue()

# Start of the main program
while True:
    clear_console()

    print(f"         HAB Taxi Services")
    print(f"         Company Services System")
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
        choice = int(input("         Enter choice (1-9): "))
    except:
        print()
        input("Invalid selection - must choose an option between 1-9. Press enter to continue...")
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
                gen_driver_fin_listing("7. Print Driver Financial Listing")
            if choice == 8:
                gen_employee_listing("8. Print Employee Listing")
            if choice == 9:
                clear_console()
                print("Thank you for using our program. Have a great day!")
                print()
                break
        else:
            print()
            input(
                "Invalid selection - must choose an option between 1-9. Press enter to continue...")

# Write constants back to defaults file
f = open("Defaults.dat", "w")
f.write(f"{NEXT_TRANS_NUM}\n")
f.write(f"{NEXT_DRIVER_NUM}\n")
f.write(f"{MONTHLY_STAND_FEE}\n")
f.write(f"{DAILY_RENTAL_FEE}\n")
f.write(f"{WEEKLY_RENTAL_FEE}\n")
f.write(f"{HST_RATE}")
f.close()
