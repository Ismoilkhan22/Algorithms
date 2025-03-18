def findSmallest(arr):
    smallest = arr[0]
    smallest_index  = 0
    for i in range(1, len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

    """
    bu yozgan kodimiz arraylarda yani massivlarda massiving eng kichik elementini qidirishga misol buladi .
   now you can use this function  to write selection sort 
    
    """
    
# endi bu funksiyani select sort qilish uchun foydalanamiz .

def selectionSort(arr):
    newarr = []
    copiedArr = list(arr)  # copy array before  mutating 
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newarr.append(copiedArr.pop(smallest))
    return newarr

