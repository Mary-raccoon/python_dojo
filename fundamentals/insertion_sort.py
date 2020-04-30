# arr = [2,8,5,6,3,9,1,7,4]
# def insertion_sort(arr):
#     count = 0
#     for i in range(len(arr)):

#         if arr[i] > arr[i+1]:
           
#             arr[i], arr[i+1] = arr[i+1], arr[i]
            
#             print(arr)
#         count+=1
#     print(count)
# insertion_sort(arr)

def insertionSort(arr):
   for index in range(1,len(arr)):

     currentvalue = arr[index]
     position = index

     while position>0 and arr[position-1]>currentvalue:
         arr[position]=arr[position-1]
         position = position-1

     arr[position]=currentvalue

arr = [14,46,43,27,57,41,45,21,70]
insertionSort(arr)
print(arr)