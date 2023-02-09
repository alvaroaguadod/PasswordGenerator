import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_num= int(input("How many letters would you like in your password?\n"))
symbols_num= int(input("How many symbols would you like?\n"))
numbers_num= int(input("How many numbers would you like?\n"))


#Hard Level
password_list= []

for char in range(1, letters_num +1):
   password_list.append(random.choice(letters))


for num in range(1, symbols_num +1):
    password_list.append(random.choice(symbols))

for char in range(1, numbers_num +1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

pass2 = ""
for char in password_list:
    pass2 += char
print(f"Your password is: {pass2}")