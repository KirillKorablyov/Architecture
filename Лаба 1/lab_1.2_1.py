List = ['l', 'i', 's','t']
List_for_zip = [1, 2, 3, 4]

#Срезы

print(f"Срез элементов, кроме первого: {List[1:]}")
print(f"Срез элементов, кроме последнего: {List[:3]}")
print(f"Срез элементов, с шагом 2: {List[::2]}")

#Список в обратном порядке

print(f"Список в обратном порядке: {List[::-1]}")

#Вывод списка в строку через ';'

print("Вывод списка в строку через ';': ", "; ".join(List))

#Результаты операции zip

zipped_val = zip(List, List_for_zip)
zipped_list = list(zipped_val)
print(f"Создание массива кортежей: {zipped_list}")

#Примеры генератора списка

data_simple = [i for i in range(0, 10)]
print(f"Простая генерация списка: {data_simple}")

data_conditions = [i for i in range(0, 10) if i % 2 == 0]
print(f"Генерация списка с условием: {data_conditions}")

data_cycle = [i * j for i in range(0, 10) for j in range(0, 10)]
print(f"Генерация списка с циклом: {data_cycle}")

data_lists = [[i * j for i in range(0, 10)] for j in range(0, 10)]
print(f"Генерация вложенных списков: {data_lists}")