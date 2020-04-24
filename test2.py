if __name__=='__main__':
	inp=int(input("Please type a number: "))
	if inp%2==0 and inp%3==0:
		print('Your number is multiple of 2 and 3')
	elif inp%2==0:
		print("Your number is a multiple of 2")
	elif inp%3==0:
		print("Your number is a multiple of 3")
	else:
		print("Your number is nor multiple of 2 and nor of 3")