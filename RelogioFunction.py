def converter(hora):
	if (hora > 12 and hora != 24):
		contador = 0
		for x in range(hora):
			if x >= 12:
				contador+=1
		return contador
	elif (hora == 24):
		print('00:00')
	else:
		return hora

print(converter(22))

