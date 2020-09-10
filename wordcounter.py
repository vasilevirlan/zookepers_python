file_name = input('enter file path:')
with open(file_name, 'r') as file:
    file_contents = file.read()
    print('Word count:', len(file_contents.split()))
