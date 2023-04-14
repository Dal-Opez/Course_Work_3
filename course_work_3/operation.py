import datetime


class Operation():
    def __init__(self, date, operation_amount, description, where_from: str, to):
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.where_from = where_from
        self.to = to

    def get_date(self):
        """
        Преобразует дату, содержащуюся в информации об операции из формата '%Y-%m-%dT%H:%M:%S.%f'
        в формат "%d.%m.%Y"
        :return: возвращает дату в формате "%d.%m.%Y" в виде строки
        """
        date_time_obj = datetime.datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        return date_time_obj.date().strftime("%d.%m.%Y")

    def get_description(self):
        """
        :return: возвращает описание операции в виде строки
        """
        return self.description

    def convert_card(self, account_data: str):
        """
        ФУнкция принимает информацию о карте и возвращает ее зашифрованный вариант
        Excample: "Maestro 1596837868705199" -> "Maestro 1596 83** **** 5199"
        :param account_data: информация о карте
        :return: возвращает зашифрованную информацию о карте
        """
        number = []
        name = []
        new_number = []
        for i in range(len(account_data)):
            if account_data[i].isdigit():
                number.append(account_data[i])
            else:
                name.append(account_data[i])
        for i in range(6, len(number) - 4):
            number[i] = "*"
        for i in range(len(number)):
            if i % 4 == 0 and i != 0:
                new_number.append(' ')
            new_number.append(number[i])
        return ''.join(name + new_number)

    def convert_account(self, account_data):
        """
        Функция принимает информацию о счете и возвращает его зашифрованный формат
        Example: "Счет 64686473678894779589" -> "Счет **9589"
        :param account_data: информация о счете
        :return: возвращает зашифрованную информацию о карте
        """
        number = []
        name = []
        for i in range(len(account_data)):
            if account_data[i].isdigit():
                number.append(account_data[i])
            else:
                name.append(account_data[i])
        number = number[-6::]
        number[0] = "*"
        number[1] = "*"
        return ''.join(name + number)

    def get_where_from(self):
        """
        Осуществляет преобразование информации о том, откуда осуществляется перевод
        в зашифрованный формат
        :return: Возвращает информацию о карте или счете в зашифрованном формате
        """
        if self.where_from is not None:
            if "Счет" in self.where_from:
                return self.convert_account(self.where_from)
            return self.convert_card(self.where_from)

    def get_to(self):
        """
        Осуществляет преобразование информации о том, куда осуществляется перевод
        в зашифрованный формат
        :return: Возвращает информацию о карте или счете в зашифрованном формате
        """
        if "Счет" in self.to:
            return self.convert_account(self.to)
        return self.convert_card(self.to)

    def get_amount(self):
        """
        :return: возвращает сумму в виде строки
        """
        return self.operation_amount["amount"]

    def get_amount_name(self):
        """
        :return: возвращает наименование валюты
        """
        return self.operation_amount["currency"]["name"]