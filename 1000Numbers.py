while True:
    try:
        vetor = []
        stop = False

        conte = 0
        while conte < 1000:
            num = int(input())
            if num == -1:
                stop = True
                break
            vetor.append(num)
            conte += 1

        if stop:
            break

        contNum = 0
        lastNum = int(input())
        for i in range(1000):
            if vetor[i] == lastNum:
                contNum += 1

        print("{} appeared {} times".format(lastNum, contNum))
    except EOFError:
        break