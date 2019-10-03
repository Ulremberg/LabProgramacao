a1 = int(input())
a2 = int(input())
a3 = int(input())

if(a1 == a2 and a2 == a3 and a3 == a1):
    print(1)
elif(a1 == a2 and a1 != a3 or a1 == a3 and a1 != a2 or a2 == a3 and a3 != a1):
    print(3)
elif(a1 != a2 and a2 != a3 and a3 != a1):
    print(2)