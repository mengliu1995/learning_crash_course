def favorite_book(name):
    import pandas
    reader = pandas.read_csv('books.csv')
    
    idx = reader['original_title']==name
    return reader[idx]['authors'].values[0]
    #print(f'One of your favoriate book is {name}')

name = input("what's your favoriate book?")

author = favorite_book(name)
print(f'One of your favoriate book is {name} by {author}')
