import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)
from controller import controller

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
MENU, PRINT, ADD_NAME, ADD_PATRONYMIC, ADD_SURNAME, ADD_NUMBER, DELETE, SEARCH, IMPORT, EXPORT = range(10)

class bot:
    __app = None
    __token = None
    __control = None

    def __init__(self, token):
        self.__token = token
        self.__control = controller(logger)
        self.temp_data = None

    async def start(self, update : Update, context):
        self.__control.load_saved_data()
        reply_keyboard = [['/print', '/add', '/delete', '/search', '/import', '/export', '/cancel']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
        await update.message.reply_text(
            'Выберите пункт меню',
            reply_markup=markup_key)
        return MENU
    
    async def print(self, update : Update, context):
        answer = self.__control.load_print_book()
        await update.message.reply_text(answer)

    # Ветка добавления контакта
    async def add(self, update : Update, context):
        self.temp_data = []
        await update.message.reply_text("Введите имя")
        return ADD_NAME

    async def get_name(self, update : Update, context):
        text = self.check_text(update.message.text)
        if text is not None:
            self.temp_data.append(text)
            await update.message.reply_text("Хорошо! Введите отчество")
            return ADD_PATRONYMIC
        return MENU

    async def get_patronymic(self, update : Update, context):
        text = self.check_text(update.message.text)
        if text is not None:
            self.temp_data.append(text)
            await update.message.reply_text("Хорошо! Введите фамилию")
            return ADD_SURNAME
        return MENU

    async def get_surname(self, update : Update, context):
        text = self.check_text(update.message.text)
        if text is not None:
            self.temp_data.append(text)
            await update.message.reply_text("Хорошо! Введите номер")
            return ADD_NUMBER
        return MENU

    async def get_number(self, update : Update, context):
        text = self.check_text(update.message.text)
        if text is not None:
            self.temp_data.append(text)
            answer = self.__control.add_contact(self.temp_data[0], self.temp_data[1], self.temp_data[2], self.temp_data[3])
            await update.message.reply_text(answer)
            self.temp_data = None
        return MENU

    # Ветка удаления
    async def delete(self, update: Update, context):
        await update.message.reply_text("Введите id контакта для удаления") 
        return DELETE

    async def remove_by_id(self, update : Update, context):
        text = self.check_text(update.message.text)
        if text is not None:
            answer = self.__control.delete_contact(text)
            await update.message.reply_text(answer)
            return MENU
        
    # Ветка поиска
    async def search(self, update: Update, context):
        await update.message.reply_text("Введите id контакта или его фамилию для поиска") 
        return SEARCH

    async def search_by_id(self, update: Update, context):
        text = self.check_text(update.message.text)
        if text is not None:
            answer = self.__control.search_by_id(text)
            await update.message.reply_text(answer)
            return MENU

    async def search_by_surname(self, update: Update, context):
        text = self.check_text(update.message.text)
        if text is not None:
            answer = self.__control.search_by_surname(text)
            await update.message.reply_text(answer)
            return MENU

    # Ветка импорта
    async def import_data(self, update: Update, context):
        await update.message.reply_text("Введите формат файла для импорта [xml/json]") 
        return IMPORT

    async def import_json(self, update: Update, context):
        answer = self.__control.import_contacts('json')
        await update.message.reply_text(answer)
        return MENU

    async def import_xml(self, update: Update, context):
        answer = self.__control.import_contacts('xml')
        await update.message.reply_text(answer)
        return MENU

    # Ветка экспорта
    async def export_data(self, update: Update, context):
        await update.message.reply_text("Введите формат файла для экспорта [xml/json]") 
        return EXPORT

    async def export_json(self, update: Update, context):
        answer = self.__control.export_contacts('json')
        await update.message.reply_text(answer)
        return MENU

    async def export_xml(self, update: Update, context):
        answer = self.__control.export_contacts('xml')
        await update.message.reply_text(answer)
        return MENU

    # Ветка выхода
    async def cancel(self, update : Update, _):
        user = update.message.from_user
        logger.info("Пользователь %s отменил разговор.", user.first_name)
        await update.message.reply_text(
            'До свидания!', 
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END

    # Дополнительно
    def check_text(self, text):
        text = text.strip().split()
        if len(text) > 0:
            if len(text[0]) > 0:
                return text[0]
        return None



    def run(self):
        self.__app = ApplicationBuilder().token(self.__token).build()
        conv_handler = ConversationHandler (
            entry_points=[CommandHandler('start', self.start)],
            states={
                MENU: [CommandHandler('print', self.print), 
                       CommandHandler('add', self.add), 
                       CommandHandler('delete', self.delete),
                       CommandHandler('search', self.search),
                       CommandHandler('import', self.import_data),
                       CommandHandler('export', self.export_data)],
                ADD_NAME: [MessageHandler(filters.TEXT & (~ filters.COMMAND), self.get_name)],
                ADD_PATRONYMIC: [MessageHandler(filters.TEXT & (~ filters.COMMAND), self.get_patronymic)],
                ADD_SURNAME: [MessageHandler(filters.TEXT & (~ filters.COMMAND), self.get_surname)],
                ADD_NUMBER: [MessageHandler(filters.TEXT & (~ filters.COMMAND), self.get_number)],
                DELETE: [MessageHandler(filters.TEXT & (~ filters.COMMAND), self.remove_by_id)],
                SEARCH: [MessageHandler(filters.Regex('[0-9]') & (~ filters.COMMAND), self.search_by_id), MessageHandler(filters.TEXT & (~ filters.COMMAND), self.search_by_surname)],
                IMPORT: [MessageHandler(filters.Regex('json') & (~ filters.COMMAND), self.import_json), MessageHandler(filters.Regex('xml') & (~ filters.COMMAND), self.import_xml)],
                EXPORT: [MessageHandler(filters.Regex('json') & (~ filters.COMMAND), self.export_json), MessageHandler(filters.Regex('xml') & (~ filters.COMMAND), self.export_xml)],
            },
            fallbacks=[CommandHandler('cancel', self.cancel)],
        )
        self.__app.add_handler(conv_handler)
        self.__app.run_polling()