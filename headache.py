import sys


try:
    filename = sys.argv[1]
except IndexError:
    print('\033[31mNo Filename Provided\033[0m')
    sys.exit(127)

if not 'headache' == filename.split('.')[-1]:
    print('\033[31mPlease Provide A Headache File\033[0m')
    sys.exit(2)

with open(filename, 'r') as file:
    prev_counter = 65
    for line in file:
        counter = 65
        if line.startswith('#'):
            continue
        for character in line:
            if '\n' == character:
                continue
            elif '>' == character:
                print(chr(counter), end='')
            elif '\\' == character:
                print()
            elif '+' == character:
                counter += 1
            elif '-' == character:
                counter -= 1
            elif '@' == character:
                counter = 97
            elif '!' == character:
                counter = 65
            elif '^' == character:
                counter = 48
            elif '.' == character:
                counter = prev_counter
            elif '#' == character:
                break

        prev_counter = counter


