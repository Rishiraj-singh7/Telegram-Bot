import telegram.ext
with open('token.txt' , 'r') as f:
     TOKEN = f.read()


updater =telegram.ext.update(TOKEN, use_context=True)
disp = updater.dispatcher
