# PythonTelegramBotContacts

## Функционал
1. Добавление контактов в книгу контактов командой /add <Имя> <Отчество> <Фамилия> <номер>
2. Вывод меню бота командой /menu
3. Вывод списка контактов командой /print
4. Удаление контактов по их идентификатору командой /delete <id>
5. Импорт контактов из хранилища на сервере в формате json или xml командой /import_contacts <json/xml>
6. Экспорт контактов в хранилище на сервере в формате json или xml командой /export_contacts <json/xml>

## Установка
#### pip install -r requirements.txt
P.S. Рекомендуется устанавливать зависимости и разворачивать приложение с использованием виртуальной среды

## Запуск приложения
1. Создание бота с вашими учетными данными, получение API токена
2. Сохранение токена в поле token модуля main.py
3. cd src
4. python main.py
5. Послать сообщение /start созданному боту
6. Наслаждаться использованием

### Структура проекта:
  - bot.py (Основной функционал бота)
  - contact_book.py (Модель данных - книга контактов)
  - contact.py (Модель данных - класс контака в книге контактов)
  - Controller.py (Центральный узел формирования контента)
  - Handler.py (Обработка файлов json/xml)
  - main.py (Старт программы, ввод токена бота)
  - text_logger.py (Модуль логгирования программы)
  - View.py (Модуль подготовки данных для отправки пользователю)

### Разработчики проекта:
  1. Алексей https://github.com/AlexBurkh
  2. Александр https://github.com/AleksandrUshenin
