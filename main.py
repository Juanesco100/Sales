from script import register_sales, calculate_total, show_summary
# Initialize empty lists to store names and prices
sales = []
product_sales = []
# Call the function to get user input and store the result in 'data'
data = register_sales(sales, product_sales)
# Extract specific information from the returned list
product_sales = data[0]
sales = data[1]
buyer = data[2]
# Calculate the final amount using the sales list
total = calculate_total(sales)
# Display all the information on the screen
show_summary(product_sales, sales, buyer, total)
