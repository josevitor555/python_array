def sequence_find(item, collection, is_sorted):
    if not is_sorted:
        collection = sorted(collection)
    
    for value in collection:
        if item == value: # 50 > 17, então continue.
            return True
        elif item < value: # 50 < 54, então continue.
            return False

items = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
result = sequence_find(50, items, False)
print(result)
