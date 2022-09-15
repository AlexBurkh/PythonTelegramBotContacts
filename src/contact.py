class contact:
    id : int = None
    name : str = None
    patronymic : str = None
    surname : str = None
    number : str = None

    def __init__(self, id : int, name : str, patronymic : str, surname : str, number : str):
        self.id = id
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.number = number

    def edit(self, name=None, patronymic=None, surname=None, number=None):
        if name != None:
            self.name = name
        if patronymic != None:
            self.patronymic = patronymic
        if surname != None:
            self.surname = surname
        if number != None:
            self.number = number