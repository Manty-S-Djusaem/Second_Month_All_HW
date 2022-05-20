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
