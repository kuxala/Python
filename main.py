import random
#importing firstnames lastnames, opening
first = open("firstnames.txt", "r")
last = open("lastnames.txt", "r")
firstnames = []
lastnames = []
#looping each firstnames and lastnames
for i in first:
	firstnames.append(i)
for j in last:
	lastnames.append(j)
# print(firstnames)
# print(lastnames)
#removing new lines
new_firstnames = [x[:-1] for x in firstnames]
new_lastnames = [x[:-1] for x in lastnames]
#generating random firstnames lastnames
rand_firstnames = random.choice(new_firstnames)
rand_lastnames = random.choice(new_lastnames)
# print(rand_firstnames)
# print(rand_lastnames)
def fullnames():
	cap_lastnames = rand_lastnames.capitalize()
	fullnames = rand_firstnames + " " + cap_lastnames
	return ("Fullname: " + fullnames)
#global
lower_lastnames = str(rand_lastnames)
lower_lastnames = lower_lastnames.lower()
lower_firstnames = str(rand_firstnames)
lower_firstnames = lower_firstnames.lower()
def gmail():
	gmails = rand_firstnames + lower_lastnames + "@gmail.com"
	return ("Gmail: " + gmails)

# print(gmail())
# print(fullnames())
def numbers():
	numbers = []
	for i in range(0,11):
		numbers.append(i)
	# print(numbers)
	ran_num = []
	for i in range(11):
		rand_numb = random.choice(numbers)
		ran_num.append(rand_numb)
	tr_string = str(ran_num)
	tr_string = tr_string.replace(",", "")
	tr_string = tr_string.replace(" ", "")
	return ("Number: " + tr_string)

def zip_code():
	zip_codes = 0,1,2,3,4,5,6,7,8,9
	rand_zip = []
	ran_zip = []
	for i in range(0,5):
		rand_zip = random.choice(zip_codes)
		ran_zip.append(rand_zip)
	tr_string = str(ran_zip)
	tr_string = tr_string.replace(",","")
	tr_string = tr_string.replace(" ", "")
	return ("Zip: " + tr_string)

def usernames():
	username = lower_firstnames + lower_lastnames[0:4]
	return ("Username: " + username)
	
def password():
	password = lower_firstnames[0] + lower_lastnames + str(123)
	return ("Password: " + password)

print(fullnames())
print(gmail())
print(usernames())
print(password())
print(zip_code())
print(numbers())

with open('credentials.txt', 'w', encoding='utf-8') as my_file:
	# str_username = str(usernames())\

    str_password = str(password())
    str_username = str(usernames())
    str_gmail = str(gmail())
    str_fullname = str(fullnames())
    str_zip_code = str(zip_code())
    str_number = str(numbers())

    my_file.write(str_fullname + "\n")
    my_file.write(str_username + "\n")
    my_file.write(str_password + "\n")
    my_file.write(str_gmail + "\n")
    my_file.write(str_zip_code + "\n")
    my_file.write(str_number + "\n")

    my_file.close()
