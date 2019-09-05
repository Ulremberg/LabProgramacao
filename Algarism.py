number = int(input())
lastNumber = number % 10
if(number < 0):
    lastNumber += -10
print(lastNumber)