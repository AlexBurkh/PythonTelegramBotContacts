from bot import bot
import config

token = config.token
_bot = bot(token)
_bot.run()