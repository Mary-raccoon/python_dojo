arr = [2,8,5,6,3,9,1,7,4]
def selection_sort(arr):
    for i in range(0,len(arr)):
        min = arr[i]
        idx = i
        for k in range(i,len(arr)): 
            if arr[k] < min:
                min = arr[k] 
                idx = k
        arr[i], arr[idx] = arr[idx], arr[i]
        print(arr)
    return arr  
selection_sort(arr)