'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''

lst = ["class", "function", "method"]


def encoder(str):
    return f'{type(bytes(str, "utf-8"))}, {bytes(str, "utf-8")}, {len(bytes(str, "utf-8"))}'


for word in lst:
    print(encoder(word))

"""
<class 'bytes'>, b'class', 5
<class 'bytes'>, b'function', 8
<class 'bytes'>, b'method', 6
"""
