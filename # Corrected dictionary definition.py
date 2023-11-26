# Corrected dictionary definition
pricelist = {"Pen": 10, "Pencil": 5, "Eraser": 5, "Ruler": 20}

# Function to get the price of a product
def get_product_price(product_name):
    return pricelist.get(product_name, -1)

# Example usage:
product_name_to_check = "Ruler"
result = get_product_price(product_name_to_check)

if result != -1:
    print(f"The price of {product_name_to_check} is: {result}")
else:
    print(f"{product_name_to_check} not found in the pricelist.")





def update(pricelist, product, new_rate):
    # Case 1: Remove the product if rate is negative or zero and the product exists
    if new_rate <= 0 and product in pricelist:
        del pricelist[product]
    # Case 2: Update the rate if it's positive and the product exists
    elif new_rate > 0 and product in pricelist:
        pricelist[product] = new_rate
    # Case 3: Add the product-rate pair if rate is positive and the product does not exist
    elif new_rate > 0:
        pricelist[product] = new_rate

    return pricelist

# Given pricelist dictionary
pricelist = {"Pen": 10, "Pencil": 5, "Eraser": 5, "Ruler": 20}

# Test cases
updated_pricelist = update(pricelist, "Pen", 15)
print("Updated pricelist:", updated_pricelist)

updated_pricelist = update(pricelist, "Eraser", 6)
print("Updated pricelist:", updated_pricelist)

updated_pricelist = update(pricelist, "Notebook", 35)
print("Updated pricelist:", updated_pricelist)
