"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

lst = ["attribute", "класс", "функция", "type"]


def encoder(str):
    return f'{type(bytes(str, "utf-8"))}, {bytes(str, "utf-8")}, {len(bytes(str, "utf-8"))}'


for word in lst:
    print(encoder(word))

"""
<class 'bytes'>, b'attribute', 9
<class 'bytes'>, b'\xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81', 10
<class 'bytes'>, b'\xd1\x84\xd1\x83\xd0\xbd\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f', 14
<class 'bytes'>, b'type', 4

"класс", "функция" - нельзя представить в байтовом виде
"""
