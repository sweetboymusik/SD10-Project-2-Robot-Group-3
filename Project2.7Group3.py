#Creates driver financial listing for the HAB Taxi Services
#Dec 12
#Group 3


#CONSTANTS
HST = 0.15

#lists
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_7 = []
list_8 = []
list_9 = []
list_10 = []
Total_list = []



#input
driver_ID = input("Enter driver number (10 digits):  ")
while True:
    if len(driver_ID) < 10:
        print()
        print("ENTER DRIVER NUMBER")
        print()
        driver_ID = input("Enter driver number (10 digits):  ")
    else: break

start_date = input("Enter driver start date (YYYY-MM-DD):  ")
while True:
    if len(start_date) < 10:
        print()
        print("ENTER START DATE")
        print()
        start_date = input("Enter driver start date (YYYY-MM-DD):  ")
    else: break


end_date = input("Enter end date (YYYY-MM-DD):  ")
while True:
    if len(end_date) < 10:
        print()
        print("ENTER END DATE")
        print()
        end_date = input("Enter end date (YYYY-MM-DD):  ")
    else: break

print("----------------------------------------------------------------")



#transaction input
print()
print("Enter driver transactions")

Total_tax = 0
Total_total = 0
Total_amount = 0
total_trans = 0
loop_stop = "Y"
while loop_stop == "Y" or loop_stop == "Yes":
    total_trans += 1

    #validation for the trans date
    trans_date = input("Enter date of transaction (YYYY-MM-DD):  ")
    while True:
        if len(trans_date) < 10:
            print()
            print("ENTER VALID DATE")
            print()
            trans_date = input("Enter date of transaction (YYYY-MM-DD):  ")
        else: break
    
    #validation for the description
    description = input("Enter a one word description of the transaction:  ")
    while True:
        if description == "":
            print()
            print("ENTER DESCRIPTION")
            print()
            description = input("Enter a one word description of the transaction:  ")
        else: break
    
    #validation for the amount
    amount = input("Enter amount of money in transaction:  ")
    while True:
        if amount == "":
            print()
            print("ENTER AMOUNT")
            print()
            amount = input("Enter amount of money in transaction:  ")
        else: break
    


    #creates transaction ID
    trans_ID = (driver_ID[0] + driver_ID[1]) + (description.upper()[0] + description.upper()[1]) + (amount[1] + amount[0]) + (driver_ID[8] + driver_ID[9])


    #calculations
    tax = float(amount) * HST
    total = tax + float(amount)

    Total_tax += tax
    Total_total += total
    Total_amount += float(amount)

    #adds variables from loop to a list
    
    if total_trans == 1:
        list_1.append(trans_date)
        list_1.append(description)
        list_1.append(amount)
        list_1.append(trans_ID)
        list_1.append(tax)
        list_1.append(total)
    elif total_trans == 2:
        list_2.append(trans_date)
        list_2.append(description)
        list_2.append(amount)
        list_2.append(trans_ID)
        list_2.append(tax)
        list_2.append(total)
    elif total_trans == 3:
        list_3.append(trans_date)
        list_3.append(description)
        list_3.append(amount)
        list_3.append(trans_ID)
        list_3.append(tax)
        list_3.append(total)
    elif total_trans == 4:
        list_4.append(trans_date)
        list_4.append(description)
        list_4.append(amount)
        list_4.append(trans_ID)
        list_4.append(tax)
        list_4.append(total)
    elif total_trans == 5:
        list_5.append(trans_date)
        list_5.append(description)
        list_5.append(amount)
        list_5.append(trans_ID)
        list_5.append(tax)
        list_5.append(total)
    elif total_trans == 6:
        list_6.append(trans_date)
        list_6.append(description)
        list_6.append(amount)
        list_6.append(trans_ID)
        list_6.append(tax)
        list_6.append(total)
    elif total_trans == 7:
        list_7.append(trans_date)
        list_7.append(description)
        list_7.append(amount)
        list_7.append(trans_ID)
        list_7.append(tax)
        list_7.append(total)
    elif total_trans == 8:
        list_8.append(trans_date)
        list_8.append(description)
        list_8.append(amount)
        list_8.append(trans_ID)
        list_8.append(tax)
        list_8.append(total)
    elif total_trans == 9:
        list_9.append(trans_date)
        list_9.append(description)
        list_9.append(amount)
        list_9.append(trans_ID)
        list_9.append(tax)
        list_9.append(total)
    elif total_trans == 10:
        list_10.append(trans_date)
        list_10.append(description)
        list_10.append(amount)
        list_10.append(trans_ID)
        list_10.append(tax)
        list_10.append(total)
    

    #ends loop if loop_stop == "N"
    loop_stop = input("Add another transaction? (Y/N)")
    while True:
        if loop_stop == "":
            print()
            print("TYPE Y OR N")
            print()
            loop_stop = input("Add another transaction? (Y/N)")
        else: break

        

#adds stuff from smaller list to bigger list
loop_ungoer = 0
while loop_ungoer < total_trans:
    if loop_ungoer == 0:
        Total_list.append(list_1)
    elif loop_ungoer == 1:
        Total_list.append(list_2)
    elif loop_ungoer == 2:
        Total_list.append(list_3)
    elif loop_ungoer == 3:
        Total_list.append(list_4)
    elif loop_ungoer == 4:
        Total_list.append(list_5)
    elif loop_ungoer == 5:
        Total_list.append(list_6)
    elif loop_ungoer == 6:
        Total_list.append(list_7)
    elif loop_ungoer == 7:
        Total_list.append(list_8)
    elif loop_ungoer == 8:
        Total_list.append(list_9)
    elif loop_ungoer == 9:
        Total_list.append(list_10)

    loop_ungoer += 1

print(Total_list)

#OUTPUT
#for value in :

    
