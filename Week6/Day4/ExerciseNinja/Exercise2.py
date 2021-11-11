# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 09:22:25 2021

@author: illouz
"""


list1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
list2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
list3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
list4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

my_list = list1 + list2 +list3 + list4
list_First_Last = []
adding = 0

for x in range(len(my_list)):
    for y in range(x+1,len(my_list)):
        if (my_list[x] > my_list[y]):
            my_list[x],my_list[y] = my_list[y],my_list[x]
    adding += my_list[x]

print("List sorted: ",my_list)
print("Sum: ",sum)

#A list containing the first and the last numbers.
list_First_Last.append(my_list[0])
list_First_Last.append(my_list[len(my_list)-1])
print(list_First_Last)

#A list of all the numbers greater than 50.
listGreater50 = []
Greater50 = 50
for i in range(len(my_list)):
    if my_list[i] > Greater50:
        listGreater50.append(my_list[i])
print("A list of all the numbers greater than 50: ", listGreater50)

#A list of all the numbers smaller than 10.
listSmaller10 = []
Smaller10 = 10
for i in range(len(my_list)):
    if my_list[i] < Smaller10:
        listSmaller10.append(my_list[i])
print("A list of all the numbers smaller than 10: ",listSmaller10)

#A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
listNumberSquared = []
for i in range(len(my_list)):
    listNumberSquared.append(pow(my_list[i],2))
print("A list of all the numbers squared: ",listNumberSquared)

#The numbers without any duplicates
listNoDuplicata = list(dict.fromkeys(my_list))
print("A list of all the numbers squared: ",listNoDuplicata)

#The average of all the numbers
average = adding/len(my_list)
print("average: ",average)
