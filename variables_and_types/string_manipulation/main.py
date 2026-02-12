grocery_items = "milk eggs cheese bread apples"
dairy1 = grocery_items[5:9]
dairy2 = grocery_items[10:16]
bakery1 = grocery_items[17:22]
aisle = 5
new_word = dairy1 + " " + dairy2 

print(f"We have dairy and bakery items: {new_word}, and {bakery1} in aisle {aisle}")