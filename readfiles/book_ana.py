filename = 'book.txt'

try:
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'Not a file {filename}')
else:
    words = contents.split()
    num_words = len(words)
    print(f'number of words: {num_words}')