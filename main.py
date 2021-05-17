from service import *

service = Service()


def process_command(command_input):
    command_data = command_input.split()

    if command_data[0] == 'createItem':
        service.create_item(command_data[1], command_data[2], int(command_data[3]))
    elif command_data[0] == 'addInventory':
        service.add_inventory(command_data[1], command_data[2], command_data[3])
    elif command_data[0] == 'addUser':
        service.add_user(command_data[1], command_data[2])
    elif command_data[0] == 'addToCart':
        service.add_to_cart(command_data[1], command_data[2], command_data[3], int(command_data[4]))
    elif command_data[0] == 'updateCart':
        service.update_to_cart(command_data[1], command_data[2], command_data[3])
    elif command_data[0] == 'getCart':
        service.get_cart_info(command_data[1])
    elif command_data[0] == 'cartCheckOut':
        service.checkout(command_data[1])
    else:
        exit(0)


while True:
    command_input = input()
    process_command(command_input)
