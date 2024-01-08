# Hotel Online Booking
# This class is for ordering
class Hotel:
    def __init__(self, time_of_order, breakfast, lunch, snacks, dinner, price):
        self.time_of_order = time_of_order
        self.breakfast = breakfast
        self.lunch = lunch
        self.snacks = snacks
        self.dinner = dinner
        self.price = price

    # This function contains the code to select and choose the dish based on the customer's choice
    def order(self):
        # The reorder is a control variable that enables the customer to order multiple times
        reorder = "Y"
        # This empty list here is created to hold the price of the orders in each iteration for final calculation
        self.price = []
        # While loop to order multiple times hosting the control variable
        while reorder.upper() == "Y":
            print("HOTEL ONLINE BOOKING")
            print("********************")
            print("Main Menu")
            print("*********")
            # The for loop is to showcase each duration of the customer's possible time of order
            for i in self.time_of_order:
                print(i.title())
            # Choice is to ask the customer's choice of order
            choice = input("Enter Your Choice: ")
            # Code contains action to be taken when customer selects breakfast
            if choice.upper() == "BREAKFAST":
                print("\nBreak Fast Menu: ")
                # Loop displays the menu in breakfast
                for i in self.breakfast:
                    print(i.title())
                breakfast_choice = input("Choose Your BreakFast: ")
                # Code contains action to be taken when the customer selects Idli
                if breakfast_choice.upper() == "IDLI":
                    idli = ["PODI IDLI - {30r}", "SAMBAR IDLI - {47.5r}", "IDLI CHUTNEY - {31.5r}"]
                    print()
                    #  The for loop prints the varieties of Idli with the price tag
                    for i in idli:
                        print(i.title())
                    idli_choice = input("Enter your choice: ")
                    if idli_choice.upper() == "PODI IDLI":
                        # Quantity of the order is aksed upon this variable
                        quantity = int(input("Enter Your Quantity {Per Idli}: "))
                        print(f"You Have Selected {quantity}.No 'Podi Idli' price - {quantity*30}r")
                        # Cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*30
                        # Value of cost is entered in the price list
                        self.price.append(cost)
                    elif idli_choice.upper() == "SAMBAR IDLI":
                        quantity = int(input("Enter Your Quantity {Per Idli}: "))
                        print(f"You Have Selected {quantity}.No 'Sambar Idli' price - {quantity*47.5}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*47.5
                        self.price.append(cost)
                    elif idli_choice.upper() == "IDLI CHUTNEY":
                        quantity = int(input("Enter Your Quantity {Per Idli}: "))
                        print(f"You Have Selected {quantity}.No 'Idli Chutney' price - {quantity*31.5}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*31.5
                        self.price.append(cost)
                    else:
                        print("WRONG ENTRY!! Pls Try Again")
                        break
                # Code contains action to be taken place when the customer selects Dosa
                elif breakfast_choice.upper() == "DOSA":
                    dosa = ["GHEE ROAST - {30r}", "MASALA DOSA - {47.5r}", "ONION ROAST - {31.5r}"]
                    print()
                    # Prints the varieties of dosa along with it's price
                    for i in dosa:
                        print(i.title())
                    dosa_choice = input("Enter your choice: ")
                    if dosa_choice.upper() == "GHEE ROAST":
                        quantity = int(input("Enter Your Quantity {Per Dosa}: "))
                        print(f"You Have Selected {quantity}.No 'Ghee Roast' price - {quantity*30}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*30
                        self.price.append(cost)
                    elif dosa_choice.upper() == "MASALA DOSA":
                        quantity = int(input("Enter Your Quantity {Per Dosa}: "))
                        print(f"You Have Selected {quantity}.No 'Masala Dosa' price - {quantity*47.5}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*47.5
                        self.price.append(cost)
                    elif dosa_choice.upper() == "ONION ROAST":
                        quantity = int(input("Enter Your Quantity {Per Dosa}: "))
                        print(f"You Have Selected {quantity}.No 'Onion Roast' price - {quantity*31.5}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*31.5
                        self.price.append(cost)
                    else:
                        print("WRONG ENTRY!! Pls Try Again")
                        break
                # Code contains action to be taken place upon ordering Vada
                elif breakfast_choice.upper() == "VADA":
                    vada = ["MEDHU VADA - {24.5r}", "MASALA VADA - {28r}", "SAMBAR VADA - {29.5r}"]
                    print()
                    # Print the varieties of vada
                    for i in vada:
                        print(i.title())
                    vada_choice = input("Enter your choice: ")
                    if vada_choice.upper() == "MEDHU VADA":
                        quantity = int(input("Enter Your Quantity {Per Vada}: "))
                        print(f"You Have Selected {quantity}.No 'Medhu Vada' price - {quantity*24.5}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*24.5
                        self.price.append(cost)
                    elif vada_choice.upper() == "MASALA VADA":
                        quantity = int(input("Enter Your Quantity {Per Vada}: "))
                        print(f"You Have Selected {quantity}.No 'Masala Vada' price - {quantity*28}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*28
                        self.price.append(cost)
                    elif vada_choice.upper() == "SAMBAR VADA":
                        quantity = int(input("Enter Your Quantity {Per Vada}: "))
                        print(f"You Have Selected {quantity}.No 'Sambar Vada' price - {quantity*29.5}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*29.5
                        self.price.append(cost)
                    else:
                        print("WRONG ENTRY!! Pls Try Again")
                        break
                # Code contains action to be taken place whenthe customer orders pongal
                elif breakfast_choice.upper() == "PONGAL":
                    print()
                    print("Pongal - {34r}")
                    quantity = int(input("Enter Your Quantity {Per Plate}: "))
                    print(f"You Have Selected {quantity}.No 'Pongal' price - {quantity * 34}r")
                    # cost is to calculate the price of the order upon entry of quantity
                    cost = quantity * 34
                    self.price.append(cost)
                # Else condition breaks the loop in case of wrong entry
                else:
                    print("WRONG ENTRY!! Pls Try Again")
                    break
            # Code contains actions to be taken place when the customer selects lunch
            elif choice.upper() == "LUNCH":
                print("\nLunch Menu: ")
                # Prints the menu available for lunch
                for i in self.lunch:
                    print(i.title())
                lunch_choice = input("Choose Your Lunch: ")
                # Code contains action to be taken place when the customer selects meals
                if lunch_choice.upper() == "MEALS":
                    print()
                    print("Meals - {170r}")
                    quantity = int(input("Enter Your Quantity {Per Plate}: "))
                    print(f"You Have Selected {quantity}.No 'Meals' price - {quantity*170}r")
                    # cost is to calculate the price of the order upon entry of quantity
                    cost = quantity*170
                    self.price.append(cost)
                # Code contains action to be taken place when the customer orders variety rice
                elif lunch_choice.upper() == "VARIETY RICE":
                    print()
                    variety_rice = ["TOMATO RICE - {120r}", "EGG FRIED RICE - {115.5r}", "CHICKEN RICE - {125r}"]
                    # Prints the variesties of variety rice along with the price of each commodity
                    for i in variety_rice:
                        print(i.title())
                    variety_rice_choice = input("Enter your choice: ")
                    if variety_rice_choice.upper() == "TOMATO RICE":
                        quantity = int(input("Enter Your Quantity {Per Plate}: "))
                        print(f"You Have Selected {quantity}.No 'Tomato Rice' price - {quantity*120}r")
                        cost = quantity*120
                        # cost is to calculate the price of the order upon entry of quantity
                        self.price.append(cost)
                    elif variety_rice_choice.upper() == "EGG FRIED RICE":
                        quantity = int(input("Enter Your Quantity {Per Plate}: "))
                        print(f"You Have Selected {quantity}.No 'Egg Fried Rice' price - {quantity*115.5}r")
                        cost = quantity*115.5
                        # cost is to calculate the price of the order upon entry of quantity
                        self.price.append(cost)
                    elif variety_rice_choice.upper() == "CHICKEN RICE":
                        quantity = int(input("Enter Your Quantity {Per Plate}: "))
                        print(f"You Have Selected {quantity}.No 'Chicken Rice' price - {quantity*125}r")
                        cost = quantity*125
                        # cost is to calculate the price of the order upon entry of quantity
                        self.price.append(cost)
                    # Else condition breaks the loop when there is a wrong entry made by the customer
                    else:
                        print("WRONG ENTRY!! Pls Try Again")
                        break
                # Code contains action to be taken place when the customer orders Indian Breads
                elif lunch_choice.upper() == "INDIAN BREADS":
                    print()
                    indian_breads = ["CHAPATI - {30r}", "ROTI - {56.5r}", "PAROTTA - {27.5r}"]
                    # Prints the varieties of indian breads
                    for i in indian_breads:
                        print(i.title())
                    indian_bread_choice = input("Enter your choice: ")
                    if indian_bread_choice.upper() == "CHAPATI":
                        quantity = int(input("Enter Your Quantity {Per Piece}: "))
                        print(f"You Have Selected {quantity}.No 'Chapati' price - {quantity*30}r")
                        cost = quantity*30
                        # cost is to calculate the price of the order upon entry of quantity
                        self.price.append(cost)
                    elif indian_bread_choice.upper() == "ROTI":
                        quantity = int(input("Enter Your Quantity {Per Piece}: "))
                        print(f"You Have Selected {quantity}.No 'Roti' price - {quantity*56.5}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*56.5
                        self.price.append(cost)
                    elif indian_bread_choice.upper() == "PAROTTA":
                        quantity = int(input("Enter Your Quantity {Per Piece}: "))
                        print(f"You Have Selected {quantity}.No 'Parotta' price - {quantity*27.5}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*27.5
                        self.price.append(cost)
                    # Else condition breaks the loop incase of a wrong entry made by the customer
                    else:
                        print("WRONG ENTRY!! Pls Try Again")
                        break
                # Code contains the action to be taken place when the customer orders Gravy
                elif lunch_choice.upper() == "GRAVY":
                    print()
                    gravy = ["CHICKEN GRAVY - {125r}", "TANDOORI PANEER - {110.5r}", "MUSHROOM GRAVY - {100r}"]
                    # Loop prints all the varieties of Gravy
                    for i in gravy:
                        print(i.title())
                    gravy_choice = input("Enter your choice: ")
                    if gravy_choice.upper() == "CHICKEN GRAVY":
                        quantity = int(input("Enter Your Quantity {Per Serving}: "))
                        print(f"You Have Selected {quantity}.No 'Chapati' price - {quantity*125}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*125
                        self.price.append(cost)
                    elif gravy_choice.upper() == "TANDOORI PANEER":
                        quantity = int(input("Enter Your Quantity {Per Serving}: "))
                        print(f"You Have Selected {quantity}.No 'Tandoori Paneer' price - {quantity*110.5}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*110.5
                        self.price.append(cost)
                    elif gravy_choice.upper() == "MUSHROOM GRAVY":
                        quantity = int(input("Enter Your Quantity {Per Serving}: "))
                        print(f"You Have Selected {quantity}.No 'Mushroom Gravy' price - {quantity*100}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*100
                        self.price.append(cost)
                    # Else condition breaks the loop incase of a wrong entry made by the customer
                    else:
                        print("WRONG ENTRY!! Pls Try Again")
                        break
                # Else condition breaks the loop incase of a wrong entry made by the customer
                else:
                    print("WRONG ENTRY!! Pls Try Again")
                    break
            # Code contains the action to be taken when the customer orders snacks
            elif choice.upper() == "SNACKS":
                print("\nSnacks Menu: ")
                # Prints the menu available for snacks
                for i in self.snacks:
                    print(i.title())
                snacks_choice = input("Choose Your Snacks: ")
                # Code contains the action to be taken place when the customer enters chat
                if snacks_choice.upper() == "CHAT":
                    print()
                    chat = ["VADA PAV - {52r}","BHEL PURI - {59r}","SAMOSA - {47r}","PUFFS - {47r}"]
                    # Prints the varieties of chat
                    for i in chat:
                        print(i.title())
                    chat_choice = input("Enter Your Choice: ")

                    if chat_choice.upper() == "VADA PAV":
                        quantity = int(input("Enter Your Quantity {Per Piece}: "))
                        print(f"You Have Selected {quantity}.No 'Vada Pav' price - {quantity * 52}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity * 52
                        self.price.append(cost)

                    elif chat_choice.upper() == "BHEL PURI":
                        quantity = int(input("Enter Your Quantity {Per Plate}: "))
                        print(f"You Have Selected {quantity}.No 'Bhel Puri' price - {quantity * 59}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity * 59
                        self.price.append(cost)

                    elif chat_choice.upper() == "SAMOSA":
                        quantity = int(input("Enter Your Quantity {Per Piece}: "))
                        print(f"You Have Selected {quantity}.No 'Samosa' price - {quantity * 47}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity * 47
                        self.price.append(cost)

                    elif chat_choice.upper() == "PUFFS":
                        quantity = int(input("Enter Your Quantity {Per Piece}: "))
                        print(f"You Have Selected {quantity}.No 'Puffs' price - {quantity * 47}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity * 47
                        self.price.append(cost)
                    # Else condition breaks the loop incase the customer enters a wrong value or option
                    else:
                        print("WRONG ENTRY!! Pls Try Again")
                        break
                # Code contains the actions to be taken place when the customer chooses sweets
                elif snacks_choice.upper() == "SWEETS":
                    print()
                    sweets = ["KHAJU KHATLI - {23r}","GULAB JAMUN - {25r}","HALWA - {20r}"]
                    # Prints the varieties of sweets
                    for i in sweets:
                        print(i.title())
                    sweet_choice = input("Enter Your Choice: ")

                    if sweet_choice.upper() == "KHAJU KHATLI":
                        quantity = int(input("Enter Your Quantity {Per Piece}: "))
                        print(f"You Have Selected {quantity}.No 'Khaju Khatli' price - {quantity * 23}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity * 23
                        self.price.append(cost)

                    elif sweet_choice.upper() == "GULAB JAMUN":
                        quantity = int(input("Enter Your Quantity {Per Plate}: "))
                        print(f"You Have Selected {quantity}.No 'Gulab Jamun' price - {quantity * 25}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity * 25
                        self.price.append(cost)

                    elif sweet_choice.upper() == "HALWA":
                        quantity = int(input("Enter Your Quantity {Per Plate}: "))
                        print(f"You Have Selected {quantity}.No 'Halwa' price - {quantity * 20}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity * 20
                        self.price.append(cost)
                    # Else condition breaks the loop when the customer enters something wrong
                    else:
                        print("WRONG ENTRY!! Pls Try Again")
                # Else contion breaks the loop incase the customer enters a wrong value
                else:
                    print("WRONG ENTRY!! Pls Try Again")
            # Code contains the actions to be atken place when the customer enter Dinner
            elif choice.upper() == "DINNER":
                print("\nDinner Menu: ")
                # PRints the menu available for dinner
                for i in self.dinner:
                    print(i.title())
                dinner_choice = input("Choose Your dinner: ")
                # Code contains the actions to be taken place when the customer enters ice creams
                if dinner_choice.upper() == "ICE CREAMS":
                    print()
                    ice_cream = ["CHOCOLATE ICE CREAM - {93.5r}","VANILLA ICE CREAM - {98r}"]
                    # Prints the varieties of ice creams available
                    for i in ice_cream:
                        print(i.title())
                    ice_cream_choice = input("Enter Your Choice: ")

                    if ice_cream_choice.upper() == "CHOCOLATE ICE CREAM":
                        quantity = int(input("Enter Your Quantity {Per Scoop}: "))
                        print(f"You Have Selected {quantity}.No 'Chocolate Ice Cream' price - {quantity*93.5}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*93.5
                        self.price.append(cost)

                    elif ice_cream_choice.upper() == "VANILLA ICE CREAM":
                        quantity = int(input("Enter Your Quantity {Per Scoop}: "))
                        print(f"You Have Selected {quantity}.No 'Vanilla Ice Cream' price - {quantity*98}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*98
                        self.price.append(cost)
                    # Else condition breaks the loop incase the customer enters a wrong value
                    else:
                        print("WRONG ENTRY!! Pls Try Again")
                        break
                # Code contains the action to be taken place incase the customer enters beverages
                if dinner_choice.upper() == "BEVERAGES":
                    print()
                    beverages = ["LEMON JUICE - {35r}","WATERMELON JUICE - {45r}"]
                    # Prints the varieties of beverages available
                    for i in beverages:
                        print(i.title())
                    beverages_choice = input("Enter Your Choice: ")
                    if beverages_choice.upper() == "LEMON JUICE":
                        quantity = int(input("Enter You Quantity {Per Cup}: "))
                        print(f"You Have Selected {quantity}.No 'Lemon Juice' price - {quantity*35}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*35
                        self.price.append(cost)

                    elif beverages_choice.upper() == "WATERMELON JUICE":
                        quantity = int(input("Enter You Quantity {Per Cup}: "))
                        print(f"You Have Selected {quantity}.No 'Watermelon Juice' price - {quantity*45}r")
                        # cost is to calculate the price of the order upon entry of quantity
                        cost = quantity*45
                        self.price.append(cost)
                    # Else condition breaks the loop incase the custmer enters a wrong value
                    else:
                        print("WRONG ENTRY!! Pls Try Again")
                        break
                # Else condtion breaks the loop incase the customer enters a wrong value
                else:
                    print("WRONG ENTRY!! Pls Try Again")
                    break
            # This second while loop runs upon breaking of loop or once the order has been placed
            while True:
                reorder = input("\nDo You Want To Order?: (y/n): ")
                # Breaks the loop and sets the control variable true for the parent loop to run again
                if reorder.upper() == "Y":
                    print()
                    break
                # Breaks the loop but sets the control variable to false and the hence the parent loop breaks
                elif reorder.upper() == "N":
                    print()
                    break
                # Else condition reasks the control variable upon a wrong entry
                else:
                    print("WRONG ENTRY!! Pls Try Again")

# The class payment hosts the code for the payment
class Payment(Hotel):
    # The previous class is called for better usage of values such as the total price amount generated
    def __init__(self, time_of_order, breakfast, lunch, snacks, dinner, price, payment_method):
        super().__init__(time_of_order, breakfast, lunch, snacks, dinner, price)
        self.time_of_order = time_of_order
        self.breakfast = breakfast
        self.lunch = lunch
        self.snacks = snacks
        self.dinner = dinner
        self.price = price
        self.payment_method = payment_method
    # This method is for the payment procedures
    def pay(self):
        # Here payment is the control variable
        payment = input("Can We Proceed With The Payment: (y/n): ")
        while payment.upper() == "Y":
            # For loop prints the various payment methods
            for i in self.payment_method:
                print(i.title())
            # Method variable asks the user his preferance of payment
            method = input("Enter Your Payment Method: ")
            print(f"The Total Amount To Be Paid: {sum(self.price)}")
            # Code to run the actions when the customer chooses the UPI method
            if method.upper() == "UPI":
                # Asks the customer his UPI id and bank account number
                upi_id = int(input("Enter Your UPI ID: "))
                bank_account = int(input("Enter your bank account: "))
                print("The Amount Is Successfully Transferred")
                # When successfuly run the control variable is set to False to prevent the next iteration
                payment = "N"
            # Code to run the actions when the customer chooses the UPI method
            elif method.upper() == "CREDIT":
                # Asks the customer his credit card choice and the his credit card number
                credit = input("Enter Your Credit card {HDFC, ICICI, SBI...}: ")
                credit_number = int(input("Enter The Credit Card Number: "))
                print("The Amount Is Successfully Transferred")
                # When successfuly run the control variable is set to False to prevent the next iteration
                payment = "N"
            # Code to run the actions when the customer chooses the debit method
            elif method.upper() == "DEBIT":
                # Asks the customer his debit card choice and the expiry date
                debit = input("Enter your Debit card {HDFC, ICICI, SBI...}: ")
                expiry_number = input("Enter The Expiry Date {Month/Year}: ")
                print("The Amount Is Successfully Transferred")
                # When successfuly run the control variable is set to False to prevent the next iteration
                payment = "N"
            # Code to run the action when the customer chooses the cash method
            elif method.upper() == "CASH":
                print("Cash Is Accepted Upon Delivery")
                # When successfuly run the control variable is set to False to prevent the next iteration
                payment = "N"
            # Else condtion breaks the loop incase of a wrong entry by the user
            else:
                print("WRONG ENTRY!! Pls Try Again")
                break
            print("\nYour Order Is On The Way!!")
            print("Thank You For Ordering With Us")
            break

# The payment super class is called by the variable called customer
customer = Payment(["BREAKFAST", "LUNCH", "SNACKS", "DINNER"],
                   ["IDLI", "DOSA", "VADA", "PONGAL"],
                   ["Meals", "Variety Rice", "Indian Breads", "Gravy"],
                   ["Chat", "Sweets", "Beverages"],
                   ["Ice Creams", "Beverages"],
                   [],
                   ["UPI", "CREDIT", "DEBIT", "CASH"])
# The method order and pay are called cosecutively and are issued as a type of the class called customer
customer.order()
customer.pay()
