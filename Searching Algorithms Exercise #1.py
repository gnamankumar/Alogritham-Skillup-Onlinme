def search_linear(array, target):

    for i in range (len(array)):       

        if (array[i] == target):

            return i

    return None

 

target = 5

array = [1, 0, 4, 2, 3, 5]

result = search_linear(array, target)

if result is not None:

    print('Value {} found at position {} using linear search'.format(target, result+1))

else:    print('Not found')
