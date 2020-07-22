'''

Bubble Sort

'''

given_array = [21, 425, 456, 78578, 1324, 45, 7, 6879, 86, 345, 32]

def bubble_sort(arr): 
    n = len(arr) 

    for i in range(n-1): 

        for j in range(0, n-i-1): 

            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                
    return arr

print('Bubble Sorted Array : ' , bubble_sort(given_array))
