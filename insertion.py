def insertion_sort(array):

    for i in range(1, len(array)):       

        #current number to be compared

        curNum = array [i]

       #compare curNum with the sorted part of the array and insert curNum

        while i>0 and array[i-1] > curNum:

            array[i] = array[i-1]

            i = i-1

            array[i] = curNum

array=[16,23,43,1,31,8]

print('Unsorted array')

print(array)

print(' ')

insertion_sort(array)
print(' ')

print('Sorted array')

print(array)
