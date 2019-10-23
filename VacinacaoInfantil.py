ano = int(input())
periodicidade = int(input())
proximaDose1= ano + periodicidade
proximaDose2= proximaDose1 + periodicidade
proximaDose3= proximaDose2 + periodicidade
print(proximaDose1, proximaDose2, proximaDose3)
print('{} {} {}'.format(proximaDose1, proximaDose2, proximaDose3))