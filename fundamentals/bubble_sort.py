arr = [3,5,2,7,8,4,1]

def bubbleSort(arr):
    for k in range(len(arr)-1):
        for i in range(len(arr)-1-k):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)
bubbleSort(arr)