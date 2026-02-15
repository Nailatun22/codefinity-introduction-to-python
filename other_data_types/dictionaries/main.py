grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

bread_details = grocery_inventory.get("Bread")

grocery_inventory["Cookies"] = (143, "Bakery")
detail_cookies = grocery_inventory.get("Cookies")
removed_item = grocery_inventory.pop("Eggs")

print("'Bread : ' Details of Bread: ", bread_details)
print("Inventory after adding Cookies: ", grocery_inventory)
print("Inventory after removing Eggs: ", grocery_inventory)

