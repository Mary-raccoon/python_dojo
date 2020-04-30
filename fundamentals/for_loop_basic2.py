# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
# def biggie_size(list):
#     for i in range(len(list)):
#         if list[i] > 0:
#             list[i] = "big"            
#     print(list)
# biggie_size([-1, 3, 5, -5])


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# def count_positives(my_list):
#     count = 0
#     for i in range(len(my_list)):
#         if my_list[i] > 0:
#             count += 1
#     my_list[len(my_list)-1] = count      
#     print(my_list)  
# count_positives([1,6,-4,-2,-7,-2])

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
# def sum_total(a):
#     sum = 0
#     for i in a:
#         sum += i
#     print(sum)
# sum_total([6,3,-2]) 

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
# def average(a):
#     sum = 0
#     for i in a:
#         sum += i
        
#     avg = sum/len(a)
#     print(avg)
# average([1,2,3,5,9]) 


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
# def length(list):
#     print(len(list))
# length([37,2,1,-9])


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
# def minimum(a):
#     if len(a) < 1:
#         return False
#     min = a[0]
#     for i in range(len(a)):
#         if a[i] < min:
#             min = a[i]
#     print(min)
# minimum([-37,2,1,-9])

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
# def maximum(a):
#     if len(a) < 1:
#         return False
#     max = a[0]
#     for i in range(len(a)):
#         if a[i] > max:
#             max = a[i]
#     print(max)
# maximum([-37,2,1,-9, 18])


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(my_list):
    max=my_list[0]
    min=my_list[0]
    sum=0
    
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
        if my_list[i] < min:
            min = my_list[i]
        sum += my_list[i]
    avg = sum / len(my_list)    

    print({"max": max, "min": min, "sum": sum, "avg": avg, "length": len(my_list)})
ultimate_analysis([10,3,-3,11]) 


# Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
# def reverse_list(lst):
#     for i in range(int(len(lst)/2)):
#         lst[i], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[i]
#     print(lst)
# reverse_list([1,2,3,4,5])