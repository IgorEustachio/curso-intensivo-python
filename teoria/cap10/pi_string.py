filename = 'cap10/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = str()

for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))