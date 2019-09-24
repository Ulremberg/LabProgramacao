ant = 1
pro = 0

while(pro <= 50):
    print(pro)
    ant = pro + ant
    pro = ant - pro
    if(ant == 0):
        pro = pro + 1

