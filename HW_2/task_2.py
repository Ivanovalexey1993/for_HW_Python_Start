# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление  .
# Функцию hex используйте для проверки своего результата//

while True:
    try:
        number = int(input("Введите число: -> "))
        if isinstance(number, int):
            print (number)
            hex_number = (format(number, '#x'))
            result = f"Число {number} перевели из 10 системы в 16, результат {hex_number}"
            print(result)
            if hex(number) == hex_number:
                result = "верно!"
                print(result)
                break
    except ValueError:
        print("введено не число. Повторите ввод")
