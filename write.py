def New_Entry():
    ID = input('Введите ID: ')
    sirname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    father_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')

    with open('employees.csv','a', encoding='utf-8') as book:
        book.write(f'{ID}, {sirname}, {name}, {father_name}, {phone};\n')
