from contact import contact

class contact_book:
    __next_id : int = 0
    __contacts = []

    def _current_max_id(self):
        max_id = 0
        for item in self.__contacts:
            if item.id > max_id:
                max_id = item.id
        return max_id

    def add_contact(self, name       : str, 
                          patronymic : str, 
                          surname    : str, 
                          number     : str):
        if self.check_contact_data(name, patronymic, surname, number):
            self.__contacts.append(contact(self.__next_id, name, patronymic, surname, number))
            self.__next_id += 1
            
    def _import_contact(self, n_id : str, 
                             name : str, 
                             patronymic : str, 
                             surname : str, 
                             number : str):
        if self.check_contact_data(name, patronymic, surname, number, id = n_id):
            self.__contacts.append(contact(n_id, name, patronymic, surname, number))
            self.__next_id = n_id + 1

    def import_contact_list(self, contact_list):
        if len(contact_list) > 0:
            self.__contacts = []
            self.__next_id = 0
            for contact in contact_list:
                self._import_contact(contact.id, contact.name, contact.patronymic, contact.surname, contact.number)
    
    def get_by_id(self, id : int):
        result = []
        if self.check_text(id):
            for item in self.__contacts:
                if item.id == id:
                    result.append(item)
        return result

    def get_by_surname(self, surname : str):
        result = []
        if self.check_text(surname):
            for item in self.__contacts:
                if item.surname == surname:
                    result.append(item)
        return result

    def edit_contact(self, id         : int, 
                           name       : str = None, 
                           patronymic : str = None, 
                           surname    : str = None, 
                           number     : str = None):
        item = self.get_by_id(id)[0]
        item.edit(name, patronymic, surname, number)

    def delete_contact(self, id : int):
        if self.check_text(id):
            flag = False
            for item in self.__contacts:
                if item.id == id:
                    self.__contacts.remove(item)
                    flag = True
            for item in self.__contacts[id:]:
                item.id -= 1
            if len(self.__contacts) != 0:
                self.__next_id = self._current_max_id() + 1
            else:
                self.__next_id = 0
            return flag
        return False
    
    def get_sorted(self):
        return sorted([item for item in self.__contacts], key = lambda row: (row.surname,
                                                                            row.name,
                                                                            row.patronymic))

    def get_unsorted(self):
        return self.__contacts

    def check_text(self, input):
        if (input != None) and (input != ""):
            return True
        return False

    def check_contact_data(self, name, patronymic, surname, number, id = 0):
        if self.check_text(name) and self.check_text(patronymic) and self.check_text(surname) and self.check_text(number) and id >= 0:
            return True
        return False