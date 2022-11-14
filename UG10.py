def mergesort(data):
    n = len(data)
    if n < 2 :
        return data
    else: 
        mid = n // 2
        
        left = data[:mid]
        right = data[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1  
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1  
            k += 1  




list1 = [1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,1,2000,3,56]
list2 = [20,21,22,23,24,25,26,27]
list3 = [30,29,31,33,19,20,31,21,59]
mergesort(list1)
mergesort(list2)
mergesort(list3)
print(list1)
print(list2)
print(list3)