# sales.py

def register_sales(sales, product_sales):

    buyer = input("What is your name ? : ")

    number_sales = int(input("How many products would you like to buy today? : "))

    for i in range(number_sales):

        print("\nSale", i + 1)

        product = input("Product's name: ")
        price = int(input("Price: $ "))
        quantity = int(input("Quantity sale: "))

        total_sale = price * quantity

        product_sales.append(product)
        sales.append(total_sale)

        continue_buying = input("Would you like to add another product? ( yes/no ): ")

        if continue_buying == "no":
            break

    return [product_sales, sales, buyer]


def calculate_total(sales):

    total = sum(sales)

    return total


def show_summary(product_sales, sales, buyer, total):

    print("\n================== Sale summary =================")

    print("Buyer:", buyer)

    print("\nProducts sold:")

    for i in range(len(product_sales)):
        print(product_sales[i], "- total sold $:", sales[i])

    print("\nTotal recipt $ :", total)