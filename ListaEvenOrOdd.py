even = []
odd = []

for i in range(0, 20):
    number = int(input('Enter value:\n'))
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print('The values even is: {}'.format(even))
print('The value odd is: {}'.format(odd))