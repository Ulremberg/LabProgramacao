value = int(input())
magnet = []
magnet.append(input())
group = 1
biggest = 1
equals = 1
for i in range(1, value):
    magnet.append(input())
    if (magnet[i - 1] == magnet[i]):
        equals += 1
        if (equals > biggest):
            biggest += 1
    else:
        group += 1
        equals = 1
print("groups: {}, biggest: {}".format(group, biggest))