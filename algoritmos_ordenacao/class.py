from array_modules import Array, UnsortedArray

# Testando a Classe Array
# arr = Array(5, "i")
# arr[0] = 10
# arr[1] = 20
# arr[2] = 30
# arr[3] = 40
# arr[4] = 50

# print(arr)

# Testando a Classe UnsortedArray
# unsorted_arr = UnsortedArray(5, "i")
# print(unsorted_arr._max_size)
# print(len(unsorted_arr._array))

# Testando a classe Array com o método Array

arr = Array(5, 'i')
arr[0] = 20
arr[1] = 50
arr[2] = 40
arr[3] = 30
arr[4] = 10

print("Array original: {}".format(arr))

# arr.bubble_sort()
# arr.merge_sort()
# arr.insertion_sort()
# arr.selection_sort()
arr.quick_sort()
print("Array ordenado: {}".format(arr))