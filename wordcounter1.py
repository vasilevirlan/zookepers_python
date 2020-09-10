def word_count():
    file_name = input('enter file path:')
    with open(file_name, 'r') as file:
        file_contents = file.read()
        print('Word count:', len(file_contents.split()))


def sentence_count():
    file_name = input('enter file name: ')
    with open(file_name, 'r') as file:
        file_contents = file.read()
        print('Total sentence: ', file_contents.count('.')
              + file_contents.count('!') + file_contents.count('?'))


if __name__ == '__main__':
    word_count()
    sentence_count()
