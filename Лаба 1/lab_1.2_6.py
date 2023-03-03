#
# # Структура кода в Python. Основные операторы. Встроенные типы и базовые операции. Целочисленное деление.
#
# #Арифметические операторы
# print(3 + 4)
# print(3 - 4)
# print(3 * 4)
# print(3 / 4)
# print(3 ** 4)
# print(3 // 4)
# print(3 % 4)
# print(3 + 4)
# #Операторы сравнения
# print(3 < 4)
# print(3 > 4)
# print(3 <= 4)
# print(3 >= 4)
# print(3 == 4)
# print(3 != 4)
# #Операторы присваивания (Семантика присваивания.)
# a = 7
# print(a)
# a += 7
# print(a)
# a -= 7
# print(a)
# a /= 7
# print(a)
# a *= 7
# print(a)
# a %= 7
# print(a)
# a **= 7
# print(a)
# a //= 7
# print(a)
# #Логические операторы Python
# a = 7 > 7 and 2 > -1
# print(a)
# a = 7 > 7 or 2 > -1
# print(a)
# a = not(0)
# print(a)
# # Операторы принадлежности
# 'pot' in 'disappointment'
# 'pot' not in 'disappointment'
# # Операторы тождественности
# '2' is "2"
# 2 is not '2'
# # Битовые операторы Python
# print(2&3)
# print(2|3)
# print(2^3)
# print(~-3)
# print(2<<2)
# print(3>>1)
#
# #Строки и операции над ними. Список, кортеж. Операции над списками. Срезы. Генераторы списков.
#
# s1 = 'Kirill'
# s2 = 'Korablyov'
# spisok = [i for i in range(0, 10)]
# tuple = ('t', 'u', 'p', 'l', 'e')
#
# print(s1 + s2)
# print(s1 * 3)
# print(len(s1))
# print(s1[0])
# print(s1[1:3:1])
# print(s1[::-1])
#
# print(spisok.append(10))
# print(spisok.remove(10))
#
# print(spisok[0])
# print(spisok[1:3:1])
# print(spisok[::-1])
#
# #Словарь, множество.
#
# d = {i: i**2 for i in range(10)}
# print(d)
#     #lab_1.2_5
#
# # Модули (lab_1.2_x)
#
# # Классы
#
# class House():
#     """Пример класса"""
#     def __init__(self, street, number):
#         """Свойства класса"""
#         self.street = street
#         self.number = number
#
#     def build(self):
#         """Метод класса"""
#         print(f"Дом на улице {self.street} по номеру {self.number}")
#
# House_1 = House("Блюхера", 32)
# House_2 = House("Блюхера", 30)
#
# print(House_1)
# print(House_2)
#
# # Обработка исключений.
#
#
# d = {i: i**2 for i in range(10)} #Сгенерированный словарь из квадратов чисел
# k = int(input("Введите ключ элемента, к который хотите вывести на экран: "))
#
# try: #Инструкция, которая может породить исключение
#     print(f"Элемент словаря, ключ которого вы ввели: {d[k]}")
#
# except KeyError: #Перехват ошибки KeyError
#     print("Вы ввели неверный ключ!")
#
# else: #Если ошибки не было
#     print(f"Всё хорошо!")
#
# finally: #Выполняемая инструкция в любом случае
#     print("Программа завершена...")
#
# # Функции – генераторы. Оператор yield.
#
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield b
#         a, b = b, a + b
#
# x = fib(13)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))