# ============================================================
#
# ============================================================
'''
This function will load a text file.
@params		file_name, the name of the file to be loaded
@return		an uppercase string containing the data read from the file
'''
def load_text(file_name):
	file_hndl = open(file_name, "r")
	file_data = file_hndl.read()
	file_hndl.close()
	return file_data.upper()
'''
This function will save data to a text file,
@params 	file_name, the name of the file to be saved
		file_data, to data to be written to the file
@return 	none
'''
def save_text(file_name, file_data):
	file_hndl = open(file_name, "w")
	file_hndl.write(file_data)
	file_hndl.close()
'''
This function encodes the sentences
@params			a, the sentence being sent to be encoded
			b, the alphabet the sentence is being encoded to
@return 		c, the encoded sentence


'''
def encode (a,b):
	a=a.upper()#makes a value uppercase
	b=b.upper()#makes b value uppercase
	temp_b=b[0]#finds the first letter in the alphabet
	temp_a=ord("A")#finds the ascii code for 'a'
	temp_b=ord(temp_b)#finds the ascii code for the first letter of the alphabet
	string_len=len(a)#finds the length of 'a'
	c=""#creates value for c
	count=temp_b - temp_a #the difference betweent the ascii value of 'b' and 'a'
	for i in range (0,string_len):
		d=a[i]
		d=ord(d)
		if (d>=32)and(d<=64):#checks to see if the ascii for 'd' is between 32 and 64
			c=c+chr(d)
		else:
			d=(d+(count))#d is d plus the ascii difference of "b"-"a"
			if(d>90):
				temp1=a[i]#finds the ascii for a[i]
				temp1=90-ord(temp1)#ascii 90 minus temp1
				temp1=count-temp1
				d=64+temp1
			c=c+chr(d)#c+d
	return (c)
'''
@params			a, the sentence being sent to be decoded
			b, the alphabet the sentence is being decoded to
@return 		c, the decoded sentence
'''
def decode(a, b):
	a=a.upper()#doing the uppercase
	b=b.upper()
	temp_b=b[0]#finding the first letter of 'b'
	temp_a=ord("A")
	temp_b=ord(temp_b)
	string_len=len(a)#finding length of string
	c=""
	count=temp_b - temp_a
	for i in range (0,string_len):
		d=a[i]
		d=ord(d)
		if (d>=32)and(d<=64):#checking if ascii is between 32 and 64
			c=c+chr(d)
		else:		
			d=(d-(count))#d is d minus ascii of (b-a)
			if(d<65):
				d=d+count+21
			c=c+chr(d)
	return (c)
'''
@params			a, the integer being sent that the alphabet will be moved to 
		
@return 		c, the moved alphabet
'''
def caesar_cipher_alphabet(a):
	string="ABCDEFGHIJKLMNOPQURSTUVWXYZ"#the english alphabet in correct order
	string_length=len(string)#length of the alphabet 
	c=""
	for i in range(0,string_length):
		d=string[i]
		d=ord(d)#getting the ascii of d[i]
		d=d+a#adding the ascii to the value a
		if(d>90):#checking to see if the ascii value goes over 90
			d=d-26#d minus 26
		c=c+chr(d)
	return c
'''
@params			a, the keyword that the alphabet will be modified to
@return 		c, the alphabet with changed order with keyword being first
'''
def keyword_cipher_alphabet(a):
	a=a.upper()#doing the upper of 'a'
	string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"#english alphabet
	temp=string
	string_length1=len(string)#getting the length of string
	length_a=len(a)#getting the length of a, the keyword
	temp1=""
	c=""
	d=""
	for i in range (0,length_a):#for i in range of 0 to length of keyword
		string_length=len(temp)
		for j in range (0,string_length):#for j in range of 0 to length of string_length, which changes depening on keyword
			if(a[i]!=temp[j]):#used to remove the letters in the alphabet that is in the keyword
				temp1=temp1+temp[j]
			else:#gets the letters thats in the keyword, ignores the repeated letter in the keyword
				d=d+temp[j]
		temp=temp1
		temp1=""
	c=c+d+temp# add 'c' first,which is an empty string, and then adds 'd' which is the keyword and then adds the remaining alphabet

	return c 
'''
@params			none
@return 		a, the alphabet if no error exsists or will return the error
'''
def cryptogram_alphabet():
	a=input("Enter alphabet: ")#promptes and gets the alphabet from the user
	a=a.upper()
	string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"#english alphabet 
	temp=string
	string_length1=len(string)#gets the length of string
	length_a=len(a)#gets the length of a
	temp1=""
	c=""
	d=""
	for i in range (0,length_a):#for i in range of 0 to length of a
		string_length=len(temp)
		for j in range (0,string_length):#for j in range of 0 to string of length, which changes depending of repeating alphabet
			if(a[i]!=temp[j]):#finds the repeating alphabet
				temp1=temp1+temp[j]
			else:
				d=d+temp[j]
		temp=temp1
		temp1=""
	c=c+temp
	if (len(a)!=26):#checks to see if the user given alphabet is 26 letters length
		a="ERROR!!! ALPHABET DOES NOT HAVE EXACTLY 26 LETTERS"
		return a
	elif (c!=""):#if user given alphabet has a duplicate letter, it will be saved in 'c'. if c is empty then there are no duplicate letter
		a="ERROR!!! CONTAINS DUPILCATE LETTER"
		return a
	else:#if no error exsists
		return a
'''
This is the main function, responsible for the user interface,
@params		none
@return		none
'''
def main():
	initial_text=""#to save the initial text
	current_text=""#to save the current text
	current_alph=""#to save the current alphabet
	program_run=True#boolen
	print ("-----------MAIN MENU-----------")
	while(program_run==True):
		print("INITIAL: ")#prints initial text
		print(initial_text)
		print("CURRENT: ")
		print(current_text)
		user_input=input(("TYPE'LOAD', TO LOAD A FILE A FILE: "))
		user_input=user_input.lower()
		check=False
		while check==False:#if error exsits it will keep on looping till the user enteres the right input
			if(user_input!="load"):#if the user enters 'load' wrong
				print ("YOU MISSPELLED 'LOAD'")
				user_input=input(("TYPE'LOAD', TO LOAD A FILE A FILE: "))
			else:#if no error exsists
				file_name=input("Enter filename: ")
				initial_text=load_text(file_name)
				check=True

		print("FUNCTIONS: CAESAR, CRYPTOGRAM, KEYWORD ")
		check=False
		while check==False:#if error exsits it will keep on looping till the user enteres the right input
			user_function=input(("CHOOSE THE FUNCTION YOU WANT TO CREATE YOUR ALPHABET "))
			user_function=user_function.lower()
			if(user_function!="caesar")and(user_function!="cryptogram")and(user_function!="keyword"):#if user enters something other than the given functions
				print("*PLEASE ENTER THE FUNCTION CORRECTLY*")
			else:#if no error exsists
				check=True

		if(user_function=="caesar"):
			user_input=int(input("How many numbers do you shift the alphabet: "))
			while user_input<0:#if error exsits it will keep on looping till the user enteres the right input
				print("*PLEASE ENTER A VALID INTEGER (0-26)")
				user_input=int(input("How many numbers do you shift the alphabet: "))
			current_alph=caesar_cipher_alphabet(user_input)
		elif(user_function=="cryptogram"):
			current_alph=cryptogram_alphabet()
			check=False
			while(current_alph=="ERROR!!! ALPHABET DOES NOT HAVE EXACTLY 26 LETTERS") or (current_alph=="ERROR!!! CONTAINS DUPILCATE LETTER"):#if error exsits it will keep on looping till the user enteres the right input
				print(current_alph)
				current_alph=cryptogram_alphabet()
				
		elif(user_function=="keyword"):
			user_input=input("Enter the keyword for creating an alphabet: ")
			current_alph=keyword_cipher_alphabet(user_input)
		print("FUNCTIONS: ENCODE-OR-DECODE")
		user_function=input(("DO YOU WANT TO ENCODE OR DECODE: "))
		user_function=user_function.lower()
		if(user_function=="encode"):
			current_text=encode(initial_text,current_alph)#calls the encode method
		elif(user_function=="decode"):
			current_text=decode(initial_text,current_alph)#calls the decode method
		print("*********CURRENT TEXT*********")
		print(current_text)
		print("*********CURRENT ALPHABET*********")
		print(current_alph)
		user_input=input("TYPE 'SAVE', TO SAVE THE FILE: ")
		user_input=user_input.lower()
		if(user_input=="save"):
			file_name=input("Enter filename: ")
			save_text(file_name,current_text)
		user_input=input("ENTER 'QUIT' TO EXIT, PRESS ANY LETTER TO CONTINUE: ")#if user enters quit
		user_input=user_input.lower()
		if(user_input=="quit"):
			program_run=False#program_run will be changed from true to false
main()
