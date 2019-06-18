with open('pi_million_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Enter your birthday, in the form mmddyy: ')

if birthday in pi_string:
    idx = pi_string.find(birthday,0,len(pi_string))
    idx = int(idx+len(birthday))
    print(f'Your birthday is in Pi, folowwing by {pi_string[idx:idx+10]}')
else:
    print('Sorry, your birthday is not in the first million of pi.')
