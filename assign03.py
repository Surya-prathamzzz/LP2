def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


if __name__ == '__main__':
 list=[]
 n = int(input("Enter number of elements : "))
 for i in range(0, n):
     ele = int(input())
     list.append(ele)
size = len(list)
print(list)
selectionSort(list, size)
print('Sorted Array in Ascending Order:')
print(list)# Selection sort in Python