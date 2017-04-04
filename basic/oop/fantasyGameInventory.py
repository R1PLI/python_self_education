def display_inventory(inventory):    # This function is correct.
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        inventory.setdefault(added_items[i], 0)
        inventory[added_items[i]] = inventory[added_items[i]] + 1

    return inv

inv = {'gold coin': 42, 'rope': 1}
display_inventory(inv)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)