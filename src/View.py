class user_interface:
    def load_menu_text(self):

        answer = 'Телефонная книга\n================\n'
        answer += 'Команды:\n'
        answer += '/menu - Вывести меню\n'
        answer += '/print - Вывести список контактов\n'
        answer += '/add <имя> <отчество> <фамилия> <номер> - Добавить контакт\n'
        answer += '/edit <id> <number> - Изменить номер контакта\n'
        answer += '/delete <id> - Удалить контакт\n'
        answer += '/search_by_id <id> - Поиск по id\n'
        answer += '/search_by_surname <surname> - Поиск по фамилии\n'
        answer += '/import_contacts <type> - Загрузить\n'
        answer += '/export_contacts <type> - Сохранить\n'
        return answer

    def load_contacts_text_with_header(self, contacts):
        answer = ''
        answer += 'Список контактов:\n=================\n'
        for c in contacts:
            answer += self.load_contact_text(c)
        return answer

    def load_contacts_text(self, contacts):
        answer = ''
        for c in contacts:
            answer += self.load_contact_text(c)
        return answer

    def load_contact_text(self, c):
        return f'id: {c.id} Фамилия: {c.surname} Имя: {c.name} Отчетство: {c.patronymic}  номер: {c.number}\n'

    def load_contact_edited_text(self, status):
        if status:
            return "Готово! Данные контакта изменены"
        else:
            return "Изменение не удалось"

    def load_contact_deleted_text(self, status, id):
        if status:
            return f'Контакт с id: {id} удален'
        else:
            return f'Ошибка при удалении контакта по id: {id}'

    def load_contact_added_text(self, status, name, patronymic, surname, number):
        if status:
            return f'Добавлен контакт: {name} {patronymic} {surname} {number}'
        else:
            return f'Контакт не добавлен. Неполные данные'
