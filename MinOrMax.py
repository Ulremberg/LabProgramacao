
print('Welcome\nEnter -1 if end')
number = int(input("Please enter a number: "))
number_list = []

while (number != int(-1)):
    number_list.append(number)
    number = int(input("Please enter a number: "))

high = max(number_list)
low = min(number_list)

print("The highest number entered was {}\n".format(high))
print("The lowest number entered was {}\n". format(low))








