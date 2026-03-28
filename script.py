# all is into sales file 

def register_sales(sales, product_sales):

    buyer = input("What is your name ? : ") # Ask for the customer's name

    number_sales = int(input("How many products would you like to buy today? : ")) # Get the number of products to define the loop limit


    for i in range(number_sales):

        print("\nSale", i + 1) # Get details for each specific product


        product = input("Product's name: ")
        price = int(input("Price: $ "))
        quantity = int(input("Quantity sale: "))

        total_sale = price * quantity # Multiply price by quantity to get the subtotal

        product_sales.append(product)
        sales.append(total_sale) # Save the name and the total price in their respective lists

        continue_buying = input("Would you like to add another product? ( yes/no ): ")

        if continue_buying == "no": # Check if the user wants to stop before reaching the limit
            break

    return [product_sales, sales, buyer]


def calculate_total(sales): 

    total = sum(sales)  # Use the sum() function to add all numbers in the list

    return total


def show_summary(product_sales, sales, buyer, total): # Print a header for the final receipt

    print("\n================== Sale summary =================")

    print("Buyer:", buyer)

    print("\nProducts sold:")

    for i in range(len(product_sales)):
        print(product_sales[i], "- total sold $:", sales[i])

    print("\nTotal recipt $ :", total) # Print the grand total of the transaction
