import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!  # $%&*+-=?@^_.'

# Функции
def cvars_book(digits_in, lowercase_letters_in, uppercase_letters_in, punctuation_in, bad_cvars_remove):
    chars = ''
    if digits_in == 'да':
        chars += digits

    if lowercase_letters_in == 'да':
        chars += lowercase_letters

    if uppercase_letters_in == 'да':
        chars += uppercase_letters

    if punctuation_in == 'да':
        chars += punctuation

    if bad_cvars_remove == 'да':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')

    return chars

def generate_password(cvars_book, lenPW):
    password = ''
    for i in range(lenPW):
        password += random.choice(cvars_book(digits_in, lowercase_letters_in, uppercase_letters_in,
                                             punctuation_in, bad_cvars_remove))
    return password

# Данные
countPW = int(input('Сколько паролей сгенерировать?'))
lenPW = int(input('Укажите длину пароля'))
digits_in = input('Включать ли цифры 0123456789?').lower()
lowercase_letters_in = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?').lower()
uppercase_letters_in = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?').lower()
punctuation_in = input('Включать ли символы !  # $%&*+-=?@^_. ?').lower()
bad_cvars_remove = input('Исключать ли неоднозначные символы il1Lo0O ?').lower()

# Вызов функции
for _ in range(countPW):
    print(generate_password(cvars_book, lenPW))


