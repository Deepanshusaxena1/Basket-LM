from models import *


class Service:
    def __init__(self):
        self.inventory = {}
        self.items = []
        self.users = []

    def create_item(self, item_category, brand, price):
        self.items.append(Item(item_category, brand, price))
        print("item added successfully")

    def add_inventory(self, item_category, brand, quantity):
        item = self.find_item(item_category, brand)
        if item is not None:
            if item in self.inventory.keys():
                self.inventory[item] = self.inventory[item] + quantity
            else:
                self.inventory[item] = quantity
        print("item added to inventory successfully")

    def find_item(self, item_category, brand):
        for item in self.items:
            if item.item_category == item_category and item.brand == brand:
                return item
        return None

    def add_user(self, user_name, wallet_amount):
        user = User(user_name, wallet_amount)
        self.users.append(user)
        print("user added successfully")

    def find_user(self, user_name):
        for user in self.users:
            if user.user_name == user_name:
                return user
        return None

    def add_to_cart(self, user_name, item_category, brand, quantity):
        user = self.find_user(user_name)
        item = self.find_item(item_category, brand)
        if int(self.inventory[item]) >= quantity:
            user.add_to_cart(item, quantity)
            self.inventory[item] = int(self.inventory[item]) - quantity
            print("item added to cart successfully")
        else:
            print("Not enough Inventory for item")

    def update_to_cart(self, user_name, item_category, brand, quantity):
        user = self.find_user(user_name)
        item = self.find_item(item_category, brand)
        if int(self.inventory[item]) > quantity:
            self.inventory[item] = int(self.inventory[item]) + quantity
            user.update_cart(item, quantity)
            self.inventory[item] = int(self.inventory[item]) - quantity
            print("cart updated successfully")
        else:
            print("Not enough Inventory for item")

    def get_cart_info(self, user_name):
        user = self.find_user(user_name)
        cart = user.cart
        for cart_item in cart.items:
            print(cart_item.item.item_category + " " + cart_item.item.brand + " " + str(cart_item.quantity))
        print("Amount " + str(cart.find_cart_value()))

    def checkout(self, user_name):
        user = self.find_user(user_name)
        user.cart.checkout()
