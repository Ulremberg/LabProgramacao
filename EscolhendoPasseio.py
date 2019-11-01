countBoliche = 0
countCinema = 0
for i in range(7):
    e = input()
    if(e.upper()=="CINEMA"):
        countCinema += 1
    else:
        countBoliche += 1
if(countBoliche > countCinema):
    print("BOLICHE")
else:
    print("CINEMA")

