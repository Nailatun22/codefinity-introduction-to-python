# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# Slice items
candy1 = items[0:9]        # Bubblegum
candy2 = items[11:20]      # Chocolate
dry_goods = items[22:27]   # Pasta

# Slice categories
category1 = categories[0:11]    # Candy Aisle
category2 = categories[13:24]   # Pasta Aisle

# Prices as strings (as required)
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

# Print with lowercase to match expected output
print(f"we have {candy1.lower()} for {bubblegum_price} in the {category1.lower()}")
print(f"we have {candy2.lower()} for {chocolate_price} in the {category1.lower()}")
print(f"we have {dry_goods.lower()} for {pasta_price} in the {category2.lower()}")
