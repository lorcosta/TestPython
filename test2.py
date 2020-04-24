if __name__=='__main__':
	name=input("Type your name: ")
	surname=input("Type you surname: ")
	place=input("What's your place of birth?: ")
	birthday=input("When's your birthday?: ")
	age=input("What's your age?: ")
	personal_data={"Name":name,
					"Surname":surname,
					"Birth":{
						"Place":place,
						"Birthday":birthday
					},
					 "age":age
					 }
	print(f"Personal data: {personal_data['Name']} {personal_data['Surname']}, born in {personal_data['Birth']}, you are currently {personal_data['age']}")