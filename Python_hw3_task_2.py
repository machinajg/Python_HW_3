"""
В большой текстовой строке подсчитать количество встречаемых слов
и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""

import string
from collections import Counter

sent = 'The execution of a function introduces a new symbol table used for the local variables of'\
       'the function. More precisely, all variable assignments in a function store the value in the'\
        'local symbol table; whereas variable references first look in the local symbol table, then'\
       'in the local symbol tables of enclosing functions, then in the global symbol table, and finally'\
       'in the table of buit-in names. Thus, global variables and variables of enclosing functions cannot'\
        'be directly assigned a value within a function (unless, for global variables, named in a global'\
       'statement, or, for variables of enclosing functions, named in a nonlocal statement), although they'\
        'may be referenced.'
FRQ = 10
tabl = str.maketrans("", "", string.punctuation)
sent = sent.translate(tabl).lower()
new_sent = Counter(sent.split())

sort_dict = dict(sorted(new_sent.items(), key=lambda item: item[1], reverse=True))
res_dict = {k: v for i, (k, v) in enumerate(sort_dict.items()) if i < FRQ}

print('10 самых частых слов: ')
for key, value in res_dict.items():
    print(f'{key} - {value}')







