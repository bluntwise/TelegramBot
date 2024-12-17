import os 
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler


load_dotenv()

token = os.getenv('TOKEN')


async def start(update, context):
    await update.message.reply_text("""
        cite2Lannion vient te menacer de faire /site pour consulter le site pour commander !
    """)

async def site(update, context):
    await update.message.reply_text("""
        Vas COMMANDER SUR https://ballon2zipette.com/
    """)

if __name__ == '__main__':
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start',start))
    app.add_handler(CommandHandler('site',site))


    print("[...]")
    app.run_polling(poll_interval=5);