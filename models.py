class Item:
    def __init__(self, item_category, brand, price):
        self.item_category = item_category
        self.brand = brand
        self.price = price


class User:
    def __init__(self, user_name, wallet_amount):
        self.user_name = user_name
        self.wallet_amount = wallet_amount
        self.cart = Cart(self.user_name)

    def add_to_cart(self, item, quantity):
        self.cart.add_item(item, quantity)

    def update_cart(self, item, quantity):
        self.cart.update_item(item, quantity)

    def remove_item_from_cart(self, item):
        self.cart.remove_item(item)


class CartItem:

    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


class Cart:
    def __init__(self, user):
        self.user = user
        self.items = []

    def add_item(self, item, quantity):
        self.items.append(CartItem(item, quantity))

    def update_item(self, item, quantity):
        cart_item = self.find_cart_item(item)
        self.items.remove(cart_item)
        self.items.append(CartItem(item, quantity))

    def remove_item(self, item):
        cart_item = self.find_cart_item(item)
        self.items.remove(cart_item)

    def find_cart_item(self, item):
        for cart_item in self.items:
            if cart_item.item == item:
                return cart_item
        return None

    def checkout(self):
        total_value = self.find_cart_value()
        if self.user.wallet_amount > total_value:
            self.user.wallet_amount = self.user.wallet_amount - total_value

    def find_cart_value(self):
        value = 0
        for cart_item in self.items:
            value += (cart_item.item.price * cart_item.quantity)
        return value
