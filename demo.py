from models import Menu, Franchise, Business

# ----- Menus -----
brunch_items = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}

brunch_menu = Menu('Brunch', brunch_items, 11, 16)

early_bird_items = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00
}

early_bird_menu = Menu('Early Bird', early_bird_items, 15, 18)

dinner_items = {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00
}

dinner_menu = Menu('Dinner', dinner_items, 17, 23)

kids_items = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}

kids_menu = Menu('Kids', kids_items, 11, 21)

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

# ----- Franchises -----
flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)

print(brunch_menu)
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(flagship_store.available_menu(14))

# ----- Separate Business Example -----
arepa_items = {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
}

arepa_menu = Menu("Take a' Arepa", arepa_items, 10, 20)
arepas_place = Franchise('189 Fitzgerald Avenue', [arepa_menu])
my_business = Business("Take a' Arepa", [arepas_place])

print(my_business)
