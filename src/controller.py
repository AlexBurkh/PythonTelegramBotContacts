from view import user_interface
from text_logger import text_logger
from handler import _json_handler, _xml_handler
from contact_book import contact_book


class controller:
    _book = None
    _UI = None
    _logger = None
    _json_handler = None
    _xml_handler = None

    def __init__(self):
        self._book = contact_book()
        self._UI = user_interface()
        self._logger = text_logger()
        self._json_handler = _json_handler()
        self._xml_handler = _xml_handler()

    def load_saved_data(self):
        self._logger.INFO('*Загрузка сохраненных данных*')
        self.import_contacts('xml')
        # self.import_contacts('json')

    def load_menu(self):
        return self._UI.load_menu_text()

    def load_print_book(self):
        contacts = self._book.get_sorted()
        return self._UI.load_contacts_text_with_header(contacts)

    def add_contact(self, name, patronymic, surname, number):
        self._book.add_contact(name, patronymic, surname, number)
        answer = f'Добавлен контакт: {name} {patronymic} {surname} {number}'
        self._logger.INFO(answer)
        return answer

    def delete_contact(self, id):
        result = self._book.delete_contact(int(id))
        if result:
            self._logger.INFO(f'Контакт с id: {id} удален')
            return f'Готово! Контакт с id: {id} удален'
        else:
            self._logger.WARNING(f'Ошибка при удалении контакта по id: {id}')
            return f'Ошибка при удалении контакта по id: {id}'

    def edit_contact(self, id):
        id = int(id)
        if self._book

    def search_by_id(self, id):
        id = int(id)
        result = self._book.get_by_id(id)
        if (self.check_search_result(result)):
            return self._UI.load_contact_text(result[0])
        else:
            self._logger.WARNING(f'Контакт с id: {id} не найден')
            return f'Контакт с id: {id} не найден'

    def search_by_surname(self, surname):
        result = self._book.get_by_surname(surname)
        if (self.check_search_result(result)):
            return self._UI.load_contacts_text(result)
        else:
            self._logger.WARNING(f'Контакт с фамилией: {surname} не найден')
            return f'Контакт с фамилией: {surname} не найден'

    def check_search_result(self, result):
        if result == [] or result == None:
            return False
        return True

    def import_contacts(self, type):
        if type == 'json':
            self._book.import_contact_list(self.import_contacts_from_json())
            self._logger.INFO("Данные из json хранилища импортированы")
        elif type == 'xml':
            self._book.import_contact_list(self.import_contacts_from_xml())
            self._logger.INFO("Данные из XML хранилища импортированы")
        else:
            self._logger.ERROR("Некорректный тип источника данных для импорта")
        return f"Контакты из {type} хранилища успешно импортированы"

    def import_contacts_from_json(self):
        return self._json_handler.load()

    def import_contacts_from_xml(self):
        return self._xml_handler.load()

    def export_contacts(self, type):
        if type == 'json':
            self.export_contacts_to_json(self._book.get_unsorted())
            self._logger.INFO("Данные в json хранилище экспортированы")
        elif type == 'xml':
            self.export_contacts_to_xml(self._book.get_unsorted())
            self._logger.INFO("Данные в XML хранилище экспортированы")
        else:
            self._logger.ERROR(
                "Некорректный тип хранилища данных для экспорта")
        return f"Контакты в хранилище успешно экспортированы"

    def export_contacts_to_json(self, contacts):
        return self._json_handler.save(contacts)

    def export_contacts_to_xml(self, contacts):
        return self._xml_handler.save(contacts)
