"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class Error_0(ZeroDivisionError):
    def __init__(self, text):
        self.text = text

delimoe = int(input("Введите первое число: "))
delitel = int(input("Введите второе число: "))
try:
    if delitel == 0:
        raise Error_0(delitel)
    delenie = delimoe / delitel
except Error_0 as err:
    print(delimoe / int(input("На ноль делить нельзя, введите другое число:")))



