#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
# letterlist = random.sample(letters,nr_letters)
# symbollist = random.sample(symbols,nr_symbols)
# numberlist = random.sample(numbers,nr_numbers)

password0 = ""
passwordlist = []
for i in range(1, nr_letters + 1):
   # password0 = password0 + random.choice(letters)
   passwordlist.append(random.choice(letters))

for i in range(1, nr_symbols + 1):
   # password0 = password0 + random.choice(symbols)
   passwordlist.append(random.choice(symbols))

for i in range(1, nr_numbers + 1):
   # password0 = password0 + random.choice(numbers)
   passwordlist.append(random.choice(numbers))


# password = ""
# for l in letterlist:
#   password = password + " " + l

# for s in symbollist:
#   password = password + " " + s

# for n in numberlist:
#   password = password + " " + n

#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# deck = password0.split()
random.shuffle(passwordlist)                        # Shuffle a list

finalpassword = ""
for w in passwordlist:
  finalpassword = finalpassword + w

print(finalpassword)