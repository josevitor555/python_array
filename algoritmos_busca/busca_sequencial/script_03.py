def search_value(index, collection):
    comparisons = 0
    for item in collection:
        comparisons += 1
        if item == index:
            print("Número de comparações feitas: {}".format(comparisons))
            return True
        elif item < index:
            print("Número de comparações feitas: {}".format(comparisons))
    return False

list_numbers = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]

element = 11
result = search_value(element, list_numbers)
print(result)
