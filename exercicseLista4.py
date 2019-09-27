#lista 5

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

list2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

even1 = []
odd1 = []

even2 = []
odd2 = []

for number in range(len(list1)):
    if(number % 2 == 0):
        even1.append(number)
    else:
        odd1.append(number)

print('The even first list: ' + str(even1))
print('The odd first list: ' + str(odd1))

for number in range(len(list2)):
    if (number % 2 == 0):
        even2.append(number)
    else:
        odd2.append(number)

even2.reverse()
odd2.reverse()
print('The even second list: ' + str(even2))
print('The odd second list: ' + str(odd2))