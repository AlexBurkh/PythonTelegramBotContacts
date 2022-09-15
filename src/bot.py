from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from Controller import Controller

class Bot():
    __app = None
    __token = None
    _Control = Controller()

    def __init__(self, token):
        self.__token = token

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._Control.load_saved_data()
        await self.menu(update, context)

    async def menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        answer = self._Control.load_menu()
        await update.message.reply_text(answer)
    
    async def print(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        answer = self._Control.load_print_book()
        await update.message.reply_text(answer)

    async def add(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        contact_data = update.message.text.split()
        answer = self._Control.add_contact(contact_data[1], contact_data[2], contact_data[3], contact_data[4])
        await update.message.reply_text(answer)

    async def delete(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = update.message.text.split()
        answer = self._Control.delete_contact(msg[1])
        await update.message.reply_text(answer)

    async def search_by_id(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = update.message.text.split()
        answer = self._Control.search_by_id(msg[1])
        await update.message.reply_text(answer)

    async def search_by_surname(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = update.message.text.split()
        answer = self._Control.search_by_surname(msg[1])
        await update.message.reply_text(answer)

    async def import_contacts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = update.message.text.split()
        answer = self._Control.import_contacts(msg[1])
        await update.message.reply_text(answer)

    async def export_contacts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = update.message.text.split()
        answer = self._Control.export_contacts(msg[1])
        await update.message.reply_text(answer)

    def run(self):
        self.__app = ApplicationBuilder().token(self.__token).build()
        self.__app.add_handler(CommandHandler("start", self.start))
        self.__app.add_handler(CommandHandler("menu", self.menu))
        self.__app.add_handler(CommandHandler("add", self.add))
        self.__app.add_handler(CommandHandler("print", self.print))
        self.__app.add_handler(CommandHandler("delete", self.delete))
        self.__app.add_handler(CommandHandler("search_by_id", self.search_by_id))
        self.__app.add_handler(CommandHandler("search_by_surname", self.search_by_surname))
        self.__app.add_handler(CommandHandler("import_contacts", self.import_contacts))
        self.__app.add_handler(CommandHandler("export_contacts", self.export_contacts))
        self.__app.run_polling()