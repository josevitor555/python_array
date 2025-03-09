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

# arr = Array(5, 'i')
# arr[0] = 20
# arr[1] = 50
# arr[2] = 40
# arr[3] = 30
# arr[4] = 10

# print("Array original: {}".format(arr))

# arr.bubble_sort()
# arr.merge_sort()
# arr.insertion_sort()
# arr.selection_sort()
# arr.quick_sort
# print("Array ordenado: {}".format(arr))

# Criando um menu interativo


def main_menu():
    print("\n=== MENU ===")
    print("1. Criar um novo array")
    print("2. Exibir o array")
    print("3. Ordenar com Bubble Sort")
    print("4. Ordenar com Merge Sort")
    print("5. Ordenar com Insertion Sort")
    print("6. Ordenar com Selection Sort")
    print("7. Ordenar com Quick Sort")
    print("8. Sair")

def main():
    arr = None

    while True:
        main_menu()
        option = str(input("Escolha uma das opções abaixo: "))
        
        match option:
            case "1":
                size_array = int(input("Digite o tamanho do array: "))
                arr = Array(size_array, "i")

                for i in range(size_array):
                    value = int(input(f"Digitte o elemento:{i + 1}: "))
                    arr[i] = value
                print("Array criado com sucesso!")
            case "2":
                if arr is None:
                    print("Crie um Array primeiro!")
                else:
                    print("Array atual: {}".format(arr))
            case "3":
                if arr is None:
                    print("Crie um Array primeiro!")
                else:
                    arr.bubble_sort()
                    print("Array ordenado com Bubble Sort: {}".format(arr))
            case "4":
                if arr is None:
                    print("Crie um array primeiro!")
                else:
                    arr.merge_sort()
                    print("Array ordenado com Merge Sort: {}".format(arr))
            case "5":
                if arr is None:
                    print("Crie um array primeiro!")
                else:
                    arr.insertion_sort()
                    print("Array ordenado com Inserction Sort: {}".format(arr))
            case "6":
                if arr is None:
                    print("Crie um array primeiro!")
                else:
                    arr.selection_sort()
                    print("Array ordenado com Selection Sort:", arr)
            case "7":
                if arr is None:
                    print("Crie um array primeiro!")
                else:
                    arr.quick_sort()
                    print("Array ordenado com Quick Sort:", arr)
            case "8":
                print("Saindo...")
                break
            case _:
                print("Opção inválida: {}".format(option))

if __name__ == "__main__":
    main()

# End