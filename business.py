from datetime import datetime

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item]
      else:
        print(f"{item} is not available in the {self.name} menu.")
        print("Please check the list of items on the bill.")
        continue
    return f"{self.name}: The bill is ${bill}."

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f"Restaurant address: {self.address}"

  def parse_time(self, time_str):
    """
    Parse time string to datetime object.
    Example: "8AM" -> datetime object with time set to 08:00:00
    """
    return datetime.strptime(time_str, "%I%p")

  def is_menu_available(self, menu, current_time):
    """
    Check if the store is open at the given time.
    """
    menu_start_time = self.parse_time(menu.start_time)
    menu_end_time = self.parse_time(menu.end_time)
    current_time = self.parse_time(current_time)
    return menu_start_time <= current_time <= menu_end_time

  def available_menus(self, time):
    menus_available = []
    menu_items_available =[]
    for menu in self.menus:
      if self.is_menu_available(menu, time):
        menus_available.append(menu.name)
        menu_items_available += (list(menu.items.keys()))
    print("The following menus are available at {} at {}: {}".format(self.address, time, menus_available))
    return menu_items_available
    #for menu in menus_available:
    #  for menu_item in menu.items:
    #    print(menu_item)

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  }
brunch = Menu("Brunch", brunch_items, "11am", "4pm")
print(brunch)
print(brunch.items)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
  }
early_bird = Menu("Early Bird", early_bird_items, "3pm", "6pm")
print("\n" + str(early_bird))
print(early_bird.items)
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.0, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}
dinner = Menu("Dinner", dinner_items, "5pm", "11pm")
print("\n" + str(dinner))
print(dinner.items)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("Kids", kids_items, "11am", "9pm")
print("\n" + str(kids))
print(kids.items)
print("\n")
flagship_store = Franchise("123 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(flagship_store)
print(new_installment)

#print(flagship_store.parse_time("8pm"))
#print(flagship_store.is_menu_available(flagship_store.menus[0], "12pm"))
print("The list of available itms are as follows: {}\n".format(flagship_store.available_menus("12pm")))
print("The list of available itms are as follows: {}".format(new_installment.available_menus("5pm")))

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
print(first_business.name)
print(first_business.franchises)

arepas_menu_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a’ Arepa", arepas_menu_items, "10am", "8pm") 
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
second_business = Business("Take a' Arepa", [arepas_place])