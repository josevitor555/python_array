import array
from typing import Union

class Array:
    '''Return a new array whose items are restricted by typecode, and
       that can contain at most `size` elements.

       Arrays behave very much like Python list, except that
       the type of objects stored in them is constrained. The type is specified
       at object creation time by using a type code, which is a single character.
       The following type codes are defined:

           Type code   C Type             Minimum size in bytes
           'b'         signed integer     1
           'B'         unsigned integer   1
           'u'         Unicode character  2
           'h'         signed integer     2
           'H'         unsigned integer   2
           'i'         signed integer     2
           'I'         unsigned integer   2
           'l'         signed integer     4
           'L'         unsigned integer   4
           'q'         signed integer     8
           'Q'         unsigned integer   8
           'f'         floating point     4
           'd'         floating point     8

        Parameters:
            max_capacity (int): The maximum number of elements the array can hold.
            typecode (str, optional): The typecode of the array. Defaults to 'l' for int.

       '''

    def __init__(self, size: int, typecode: str = 'l'):
        if size <= 0:
            raise ValueError(f'Invalid array size (must be positive): {size}')
        self._size = size
        self._array = array.array(typecode, [0] * size)

    def __len__(self):
        return self._size

    def __getitem__(self, index: int) -> Union[int, float]:
        if index < 0 or index >= self._size:
            raise IndexError('array index out of range')
        return self._array[index]

    def __setitem__(self, index: int, val: Union[int, float]) -> None:
        if index < 0 or index >= self._size:
            raise IndexError('array assignment index out of range')
        self._array[index] = val

    def __repr__(self):
        return repr(self._array)

    # Bubble Sort Method (Classificação por bolha)
    def bubble_sort(self):
        n = self._size
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self._array[j] > self._array[j + 1]:
                    self._array[j], self._array[j + 1] = self._array[j + 1], self._array[j]
                    swapped = True
            
            if not swapped:
                break
    
    # Merge Sort Method (Classificação por mesclagem)
    def merge_sort(self):
        def _merge_sort(left, right):
            if left < right:
                mid = (left + right) // 2
                _merge_sort(left, mid)
                _merge_sort(mid + 1, right)
                merge(left, mid, right)

        def merge(left, mid, right):
            L = [self[i] for i in range(left, mid + 1)]
            R = [self[i] for i in range(mid + 1, right + 1)]
            
            i = j = 0
            k = left

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    self[k] = L[i]
                    i += 1
                else:
                    self[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                self[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                self[k] = R[j]
                j += 1
                k += 1

        _merge_sort(0, self._size - 1)

    # Insertion sort Method (Classificação por inserção)
    def insertion_sort(self):
        for i in range(1, len(self)):
            key = self[i]
            j = i - 1

            while j >= 0 and self[i] > key:
                self[i + 1] = self[i]
                j = j - 1
            self[j + 1] = key
    
    # Selection Sort Method (Classificação baseado em comparação)
    def selection_sort(self):
      n = len(self)
      for i in range(n):
        min_index = i
        for j in range(i + 1, n):
          if self[j] < self[min_index]:
            min_index = j
        self[i], self[min_index] = self[min_index], self[i]
    
    # Queick Sort (Clasificiação baseada em dividir e conquistar)
    def quick_sort(self):
      def _quick_sort(low, high):
        if low < high:
          pi = partition(low, high) # pi = partition index = 2
          _quick_sort(low, pi - 1)
          _quick_sort(pi + 1, high)

      def partition(low, high):
        pivot = self[high]
        i = low - 1

        for j in range(low, high):
          if self[j] <= pivot:
            i = i + 1
            self[i], self[j] = self[j], self[i]
        self[i + 1], self[high] = self[high], self[i + 1]
        return i + 1

      _quick_sort(0, len(self) - 1)

class UnsortedArray:
    def __init__(self, max_size, typecode = 'l'):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0
