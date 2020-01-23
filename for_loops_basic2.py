#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(num):
    for i in range(len(num)):
        if (num[i] > 0):
            num[i] = "big"
    print(num)
    return num
#biggie_size([-1, 3, 5, -5])

#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(pos):
    counter = 0
    for i in range(len(pos)):
        if(pos[i]> 0 ):
            counter = counter + 1
    pos[-1] = counter
    print(pos)
count_positives([-1,1,1,1])
count_positives([1,6,-4,-2,-7,-2])

#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
def sum_total(arg):
    counter = 0
    for i in range(len(arg)):
         counter = arg[i] + counter
    print(counter)
    return counter
sum_total([1,2,3,4])
sum_total([6,3,-2])

#Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
def average(num):
    counter = 0
    for i in range(len(num)):
        counter = num[i] + counter
    avg = counter / len(num)
    print(avg)
average([1,2,3,4])

#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
def length(my_len):
    if (len(my_len) <= 1):
        return False
    print(len(my_len))
    return len(my_len)
length([37,2,1,-9])
length([])

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False
def minimum(num):
    if(len(num) <= 1):
        print(False)
        return False
    low = num[0]
    for i in range(len(num)):
        if(num[i] < low):
            low = num[i]
    print(low)
minimum([37,2,1,-9])
minimum([])

#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
def maximum(num):
    max = 0
    if (len(num) <= 1):
        return False
    for i in range(len(num)):
        if(num[i] > max):
            max = num[i]
    print(max)
maximum([37,2,1,-9])
maximum([])

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(num):
    new_list = {}
    counter = 0
    low = num[0]
    max = 0
    for i in range(len(num)):
        if(num[i] > max):
            max = num[i]
        elif(num[i] < low):
            low = num[i]
        counter = counter + num[i]
        avg = counter / len(num)
    new_list['sumTotal'] = counter
    new_list['average'] = avg
    new_list['minimum'] = low
    new_list['maximum'] = max
    new_list['length'] = len(num)
    print(new_list)
ultimate_analysis([37,2,1,-9])

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(lst):
    temp = 0
    temp = lst[-1]
    lst[-1] = lst[0]
    lst[0] = temp
    temp = lst[-2]
    lst[-2] = lst[1]
    lst[1] = temp
    print(lst)
reverse_list([37,2,1,-9])
