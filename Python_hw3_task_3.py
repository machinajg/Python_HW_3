"""
       Создайте словарь со списком вещей для похода в качестве ключа и их массой
       в качестве значения. Определите какие вещи влезут в рюкзак передав его
       максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
       *Верните все возможные варианты комплектации рюкзака.
"""

equip = {'c: 1.5, 'raincoat': 0.5, 'rubber_boots': 2.0,
         'socks': 0.1, 'thermal_underwear': 0.4, 'flashlight': 0.4,
         'food': 2.5, 'water': 2.0, 'bowl': 0.2, 'mug': 0.2, 'spoon': 0.1,
         'knife': 0.3, 'matches': 0.05, 'tent': 15.0}

BAG_PACK = 20.0
weight = 0.0

#Вариант 1: Сортировка по возрастанию
slct_asc = []
equip_asc = dict(sorted(equip.items(), key=lambda item: item[1]))
#print(equip_asc)
for k, v in equip_asc.items():
       if weight + equip_asc[k] < BAG_PACK:
              weight += equip_asc[k]
              slct_asc.append(k)

print('Selected equipment: ' + ', '.join(slct_asc))
print(f"Bag pack's weight: {weight} kg")

#Вариант 2: Сортировка по убыванию
slct_dsc = []
equip_dsc = dict(sorted(equip.items(), key=lambda item: item[1], reverse=True))
#print(equip_dsc)
for k, v in equip_dsc.items():
       if weight + equip_dsc[k] < BAG_PACK:
              weight += equip_dsc[k]
              slct_dsc.append(k)

print('Selected equipment: ' + ', '.join(slct_dsc))
print(f"Bag pack's weight: {weight} kg")