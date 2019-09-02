seg = int(input())

horas = seg //3600

rem = seg % 3600

min = rem // 60

segundos = rem % 60

print("{}"':'"{}"':'"{}" .format(horas, min, segundos))