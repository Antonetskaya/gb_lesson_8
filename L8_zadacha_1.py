"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных"""


class Date:
    def __init__(self, data=str):
        self.data = data

    @classmethod
    def classmethod(cls, data):
        data_v_choslo = data.split("-")
        d = int(data_v_choslo[0])
        m = int(data_v_choslo[1])
        y = int(data_v_choslo[2])
        return f'День: {d} месяц: {m} год: {y}'

    @staticmethod
    def staticmethod(d, m, y):
        if 1 > d or d > 31:
            return 'Неверно указан день'
        elif 1 > m or m > 12:
            return 'Неверно указан месяц'
        elif 2022 < y or y < 1:
            return 'Неверно указан год'
        else:
            return f'День: {d} месяц: {m} год: {y}'

data_str = '05-12-1988'
print(Date.classmethod(data_str))
print(Date.staticmethod(2, 10, 1988))
print(Date.staticmethod(18, 22, 1988))
print(Date.staticmethod(48, 5, 1988))
print(Date.staticmethod(12, 5, 2023))
