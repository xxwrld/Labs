lib ={}


while True:
    n = input('Яка потрібна дія ?\n1 - дізнатись значення за ключем\n2 - вивести весь список\n3 - додати нову книгу\n'
              '4 - анігілірувати книгу\nend - закінчити роботу\n')
    if n == '1':
        key1 = input('ключ -  ')
        print(lib[key1])
    elif n == '2':
        print(lib)
    elif n == '3':
        key = input('тег нової книги - ')
        author = input('автор - ')
        name = input('назва - ')
        edition = input('видавництво - ')
        genre = input('жанр - ')
        year = input('рік - ')
        special_literature = input('належить до спеціальної літератури - ')
        hobby = input('належить до хоббі - ')
        origin = input('походження книги - ')
        availability = input('наявність - ')
        lib[key]={'book data': {
                'author': author,
                'name': name,
                'edition': edition,
                'genre': genre,
                'year': year
                },
            'lib section': {
                'special literature': special_literature,
                'hobby': hobby
                },
            'origin': origin,
            'availability': availability}
    elif n=='4':
        key=input('яку книгу видалити?')
        del lib[key]
    elif n == 'end':
        break
    else:
        raise Exception('Некоректне значення дії')
