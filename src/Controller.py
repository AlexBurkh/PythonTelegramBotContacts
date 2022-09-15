from View import UserInterface
from text_logger import text_logger
from Handler import JsonHandler, XMLHandler
from contact_book import contact_book

class Controller:
    _Book = None
    _UI = None
    _Logger = None
    _JsonHandler = None
    _XMLHandler = None


    def __init__(self):
        self._Book = contact_book()
        self._UI = UserInterface()
        self._Logger = text_logger()
        self._JsonHandler = JsonHandler()
        self._XMLHandler = XMLHandler()

    def load_saved_data(self):
        self._Logger.INFO('*Загрузка сохраненных данных*')
        self.import_contacts('xml')
        #self.import_contacts('json')

    def load_menu(self):
        return self._UI.load_menu_text()

    def load_print_book(self):
        contacts = self._Book.get_sorted()
        return self._UI.load_contacts_text_with_header(contacts)

    def add_contact(self, name, patronymic, surname, number):
        self._Book.add_contact(name, patronymic, surname, number)
        answer = f'Добавлен контакт: {name} {patronymic} {surname} {number}'
        self._Logger.INFO(answer)
        return answer

    def delete_contact(self, id):
        result = self._Book.delete_contact(int(id))
        if result:
            self._Logger.INFO(f'Контакт с id: {id} удален')
            return f'Готово! Контакт с id: {id} удален'
        else:
            self._Logger.WARNING(f'Ошибка при удалении контакта по id: {id}')
            return f'Ошибка при удалении контакта по id: {id}'

    def search_by_id(self, id):
        id = int(id)
        result = self._Book.get_by_id(id)
        if (self.check_search_result(result)):
            return self._UI.load_contact_text(result[0])
        else:
            self._Logger.WARNING(f'Контакт с id: {id} не найден')
            return f'Контакт с id: {id} не найден'

    def search_by_surname(self, surname):
        result = self._Book.get_by_surname(surname)
        if (self.check_search_result(result)):
            return self._UI.load_contacts_text(result)
        else:
            self._Logger.WARNING(f'Контакт с фамилией: {surname} не найден')
            return f'Контакт с фамилией: {surname} не найден'
    
    def check_search_result(self, result):
        if result == [] or result == None:
            return False
        return True

    def import_contacts(self, type):
        if type == 'json':
            self._Book.import_contact_list(self.import_contacts_from_json())
            self._Logger.INFO("Данные из json хранилища импортированы")
        elif type == 'xml':
            self._Book.import_contact_list(self.import_contacts_from_xml())
            self._Logger.INFO("Данные из XML хранилища импортированы")
        else:
            self._Logger.ERROR("Некорректный тип источника данных для импорта")
        return f"Контакты из {type} хранилища успешно импортированы"

    def import_contacts_from_json(self):
        return self._JsonHandler.load()

    def import_contacts_from_xml(self):
        return self._XMLHandler.load()

    def export_contacts(self, type):
        if type == 'json':
            self.export_contacts_to_json(self._Book.get_unsorted())
            self._Logger.INFO("Данные в json хранилище экспортированы")
        elif type == 'xml':
            self.export_contacts_to_xml(self._Book.get_unsorted())
            self._Logger.INFO("Данные в XML хранилище экспортированы")
        else:
            self._Logger.ERROR("Некорректный тип хранилища данных для экспорта")
        return f"Контакты в хранилище успешно экспортированы"

    def export_contacts_to_json(self, contacts):
        return self._JsonHandler.save(contacts)

    def export_contacts_to_xml(self, contacts):
        return self._XMLHandler.save(contacts)