from itertools import product

def combos(m, n): #Функция, возвращающая сочетания двух списков
    return list(product(m, n)) # m - список 1, n - список 2;

m = (input("Введите список m: "). split())
n = (input("Введите список n: "). split())

print(f"Всевозможные комбинации чисел, содержащихся в списках m и n,  по k чисел:\n {combos(m, n)}")