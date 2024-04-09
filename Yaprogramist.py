eng2sp = dict()  # создаем пустой словарь
print(eng2sp)  # выведет {}
eng2sp['one'] = 'uno'  # добавляем 'uno' для элемента с ключом 'one'
print(eng2sp)  # выведет {'one': 'uno'}
print(eng2sp['one'])  # выведет 'uno'
eng2sp['two'] = 'dos'  # добавляем 'dos' для элемента с ключом 'two'
eng2sp['three'] = 'tres'  # добавляем 'tres' для элемента с ключом 'three'
print(eng2sp)  # выведет {'three': 'tres', 'one': 'uno', 'two': 'dos'}, порядок пар может быть другим
