# Busca birnária usando recursividade
def binary_search(list_elements, x, low=0, high=None):

    if high is None:
        high = len(list_elements) - 1
    
    if low > high:
        return False # Caso base: Não encontrou o item

    mid_list = (low + high) // 2

    if list_elements[mid_list] == x:
        return True
    elif x > list_elements[mid_list]:
        return binary_search(list_elements, x, mid_list + 1, high) # Buscando na metade direita
    else:
        return binary_search(list_elements, x, low, mid_list - 1) # Buscando na metade esqueda

list_elements = [91, 90, 57, 17, 50, 3, 13, 8, 11, 22, 33, 44, 10]
sorted_list = sorted(list_elements)
print(sorted_list)

element = 90
print(binary_search(sorted_list, element, 0, len(sorted_list) - 1))
