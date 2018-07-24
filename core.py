def process_inventory(unprocessed_inventory):
    '''(list of str) -> list of dict

    Returns a list of inventory items as a list of inventory dictionaries
    '''
    inventory_list = []
    for item in unprocessed_inventory:
        item = item.strip().split(',')
        item_dict = dict(
            item_name=item[0],
            base_rental_price=int(item[1]),
            replacement_cost=int(item[2]),
            in_stock=int(item[3]),
            initial_stock=int(item[4]))
        inventory_list.append(item_dict)
    return inventory_list
