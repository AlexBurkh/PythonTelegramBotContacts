# PythonTelegramBotContacts

## Функционал
1. Добавление контактов в книгу контактов командой /add <Имя> <Отчество> <Фамилия> <номер>
2. Вывод меню бота командой /menu
3. Вывод списка контактов командой /print
4. Изменение номера контакта командой /edit <id> <number>
5. Удаление контактов по их идентификатору командой /delete <id>
6. Импорт контактов из хранилища на сервере в формате json или xml командой /import_contacts <json/xml>
7. Экспорт контактов в хранилище на сервере в формате json или xml командой /export_contacts <json/xml>

## Установка
#### pip install -r requirements.txt
P.S. Рекомендуется устанавливать зависимости и разворачивать приложение с использованием виртуальной среды

## Запуск приложения
1. Создание бота (у бота https://t.me/BotFather) с вашими учетными данными, получение API токена
2. cd src
3. Сохранение токена в поле token модуля main.py
4. python main.py
5. Послать сообщение /start созданному боту
6. Наслаждаться использованием

### Структура проекта:
  - bot.py (Основной функционал бота)
  - contact_book.py (Модель данных - книга контактов)
  - contact.py (Модель данных - класс контакта в книге контактов)
  - controller.py (Центральный узел формирования контента)
  - handler.py (Обработка файлов json/xml)
  - main.py (Старт программы, ввод токена бота)
  - text_logger.py (Модуль логгирования программы)
  - view.py (Модуль подготовки данных для отправки пользователю)

### Разработчики проекта:
  1. Алексей https://github.com/AlexBurkh
  2. Александр https://github.com/AleksandrUshenin
