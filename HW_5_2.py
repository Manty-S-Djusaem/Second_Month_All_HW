import re


class ValidCarNumber:
    def is_valids(self, number):
        numb = re.match(r'^(\d{2})+([A-Z]{2})+(\d{3})+([A-Z]{3})', number)
        if numb:
            print('Номер валидный!')
        else:
            print('Номер не валидный!')


car = ValidCarNumber()
car.is_valids('01KG777BMW')
car.is_valids('1234sdfghj')
car.is_valids('12DF123DF')

# написать валидацию на Номера Транспартов
# будет класс ValidCarNumber —> будет метод is_valid(self, number)
# который принимает 1 аргумент number и проверяет на валидность то есть:
# Input:
#
#     01KG777BAD
#     hhh777hhh
#
# Output:
#
#     Номер валидный!
#     Номер не валидный!
# number = input("Введите номер машины: ")
# is_valid = re.search(r"[A-Z0-9]", number)
#
# if number == is_valid:
#     print("Ok")
# elif number != is_valid:
#     print("No")


# if not is_valid:
#     print("Write the valid number")
# elif number[is_valid.start():is_valid.end()] == number:
#     print("number Valid")
# pattern = r"[a-zA-Z]"
