def list_inventory(inventory):
    if not inventory:
        print("Inventory is empty")
    else:
        print("Inventory: ")
        for x in inventory:
            print(x.name)