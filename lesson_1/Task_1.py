'''
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат
Unicode и также проверить тип и содержимое переменных.
'''

lst = ['разработка', 'сокет', 'декоратор']

for word in lst:
    print(f'{word} , type={type(word)}  {word.encode("utf-8")}, type={type(word.encode("utf-8"))}')


"""
разработка , type=<class 'str'>  b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0', type=<class 'bytes'>
сокет , type=<class 'str'>  b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82', type=<class 'bytes'>
декоратор , type=<class 'str'>  b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80', type=<class 'bytes'>
"""