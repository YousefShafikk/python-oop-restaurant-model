class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time


  def calculate_bill(self, purchased_items):
  """
  Calculate the total bill for a list of purchased items.
  Items not found on the menu are ignored.
  """
  bill = 0
  for item in purchased_items:
    if item in self.items:
      bill += self.items[item]
  return bill


  def __repr__(self):
    return f"{self.name} menu is available from {self.start_time} to {self.end_time}"




class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus # list of Menu objects
  def available_menu(self, time):
    """
    Return a list of menus available at a given time.
    """
    return [menu for menu in self.menus if menu.start_time <= time <= menu.end_time]


  def __repr__(self):
    return f"Franchise located at {self.address}"




class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises # list of Franchise objects


  def __repr__(self):
    return f"Business: {self.name}"
