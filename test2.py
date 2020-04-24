if __name__=='__main__':
	numbers=[1,2,3,4,5,6,7,8,9,10]
	sommaNumeri=0
	lunghezza=len(numbers)
	for item in numbers:
		sommaNumeri+=item
	print(f'la media tra i numeri da 1 a 10 è {sommaNumeri/lunghezza}')
	maxValue=0
	for item in numbers:
		if item>maxValue:
			maxValue=item
	print(f'Il valore massimo tra i numeri da 1 a 10 è {maxValue}')
	minValue=100
	for item in numbers:
		if item<minValue:
			minValue=item
	print(f'Il valore minimo tra i numeri da 1 a 10 è {minValue}')
	

