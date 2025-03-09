list_elements = [10, 44, 33, 22, 50, 3, 13, 8, 11, 11, 57, 90, 91]
# A busca sequencial tem uma complexidade de O(n), ou seja, o tempo de execução está ligado diretamente ao tamanho da lista.

def found_element(element):
    for item in list_elements:
        if element == item:
            return True
    return False

element = 444
if found_element(element):
    print("Found: {}".format(element))
else:
    print("Element not found: {}".format(element))