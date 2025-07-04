'''Write a function restock_inventory() that updates an inventory dictionary based on a restock list. It accepts two parameters:

current_inventory: a dictionary where each key-value pair represents an item and its current stock in the inventory
restock_list: a dictionary where each key-value pair represents an item and the quantity to be added to the inventory
If an item in restock_list is not present in the current_inventory, it should be added. The function should return the updated dictionary current_inventory.

def restock_inventory(current_inventory, restock_list):
    pass
Example Input:

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
Example Output:

current_inventory = {
    "apples": 40,
    "bananas": 15,
    "oranges": 30,
    "pears": 5
}'''

def restock_inventory(curr_inv, restock_inv):
    for k, v in restock_inv.items():
        if k in curr_inv.keys():
            curr_inv[k] += v
        else:
            curr_inv[k] = v


current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

restock_inventory(current_inventory, restock_list)

print(current_inventory)