print('Wellcome to KBC')
def Quit():
	exit()
questions=['What is the capital of Australia?','Which is the longest river in the world?','What is the capital of India?','What is the name of captain of Indian cricket team?','What is the capital of Madhya Pradesh?','What is the name of Cheif Minister of Uttar Pradesh?']
options=['A:Sydney , B:Canberra ,C:Perth , D:Brisbane','A:Brahamputra , B:Amazon , C:Nile , D:Ganga','A:Mumbai , B:Kolkata , C:Chennai , D:Delhi','A:Rohit Sharma , B:Virat Kohli , C:Rishanbh Pant , D:Ravindra Jadeja','A:Indore , B:Jabalpur , C:Katni , D:Bhopal','A:Narendra Damodardas Modi , B:Yogi Aadityanath , C:Arvind Kejariwal , C:Shivraj Singh Chauhan']
correctoptions=['B','C','D','B','D','B']
price=['0','10000','100000','2000000','4000000','8000000','10000000']
validoptions=['A','B','C','D']
n=1
while n<=6:
	print('Your question for Rs',price[n],'is')
	print('Question-',n,':',questions[n-1],'\n', options[n-1])
	print('Type 1 if you want to answer or type 2 if you want to quit.')
	while True:
		choice=int(input("Enter your choice:"))
		if choice==1:
			answer=input("Enter your option:")
			while True:
				if answer==correctoptions[n-1]:
					print('Congratulations your answer is correct and you won Rs',price[n])
				if answer!=correctoptions[n-1]:
					print('Incorrect answer, You lost !','\n','And you won Rs',price[n-1])
					Quit()
				if answer==validoptions[0] or answer==validoptions[1] or answer==validoptions[2] or answer==validoptions[3]:
					print('Enter a valid option.')
					break
		if choice==2:
			Quit()
		else:
			print('Enter a valid choice.')
			break
	n=n+1

