#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pw = ""
for _ in range(nr_letters):
	pw += random.choice(letters)
for _ in range(nr_symbols):
	pw += random.choice(symbols)
for _ in range(nr_numbers):
	pw += random.choice(numbers)
print("Your password should be " + pw)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for _ in range(nr_letters):
	letter = random.choice(letters)
	password_list.append(letter)
for _ in range(nr_symbols):
	symbol = random.choice(symbols)
	password_list.append(symbol)
for _ in range(nr_numbers):
	number = random.choice(numbers)
	password_list.append(number)

random.shuffle(password_list)
# print(password_list)
password = ""
for char in password_list:
	password += char
print(f"Your password should be {password}")
	