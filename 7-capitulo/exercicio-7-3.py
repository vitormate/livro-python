first_string = input('First string: ')
sec_string = input('Second string: ')

new_list = []


for letter in sec_string:
    if letter not in first_string and letter not in new_list:
        new_list.append(letter)

for letter in first_string:
    if letter not in sec_string and letter not in new_list:
        new_list.append(letter)

print(''.join(new_list))