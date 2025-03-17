"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

my_list = [2, 3, 'hi', 2, 14, 2, 6, 'hi', 8, 14, ':-)']
print(my_list)

new_list = []
for i in my_list:
    if my_list.count(i) >= 2:
        new_list.append(i)
print(set(new_list))

