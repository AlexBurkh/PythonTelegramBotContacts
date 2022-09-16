class contact:
    id: int = None
    name: str = None
    patronymic: str = None
    surname: str = None
    number: str = None

    def __init__(self, id: int, name: str, patronymic: str, surname: str, number: str):
        self.id = id
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.number = number

    def edit(self, number):
        if number != None and number != "":
            self.number = number
