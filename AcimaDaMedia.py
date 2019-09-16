
n1 = float(input())
n2 = float(input())
n3 = float(input())

media = ((n1 + n2 + n3) / 3.0)

if (n1 > media and n2 < media and n3 < media):
    print('1')
elif (n1 < media and n2 > media and n3 < media):
    print('1')
elif (n1 < media and n2 < media and n3 > media):
    print('1')
elif (n1 > media and n2 > media and n3 < media):
    print('2')
elif (n1 > media and n2 > media and n3 > media):
    print('3')
elif (n1 > media and n2 < media and n3 > media):
    print('2')
elif (n1 < media and n2 > media and n3 > media):
    print('2')
else:
    print('0')
