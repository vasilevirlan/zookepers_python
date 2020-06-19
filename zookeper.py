animals = ['camel', 'lion', 'deer', 'goose', 'bat', 'rabbit']
while True:
    number = input('Which habitat do you need ?')
    if number == 'exit' or int(number) > len(animals):
        print('bye')
        break
    else:
        # print('Which habitat do you need?')
        print(animals[int(number)])

