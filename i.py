import telegram.ext
import pandas_datareader as web


with open('token.txt' , 'r') as f:
     TOKEN = f.read()

def start(update, context):
    update.message.reply_text("hello! welcome to neuralbot!")

def help(update, context):
    update.message.reply_text("""
    The following commands are available:

    /start -> Welcome message
    /help -> This message
    /content -> Infomation about nueralnine content 
    /contact -> Infomation about contact
    """)

def content(update, context):
   update.message.reply_text("We have videos and books! Watch and read them!")

def content(update, context):
    update.message.reply_text(" You can contact Florian on the Discord server. ")

def stock(update, context):
    ticker = context.args[0]
    date = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text("The current price OF {ticker} is {price:.2f}$!")

def handle_message(update, context):
    update.message.reply_text(f"you said {update.message.text}")

updater =telegram.ext.update(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("stocK", stock))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()


