def printStatusBot(message_data, chat_id, message_text, mesType):
    if mesType == 0:
        print(getChatTemples(chat_id) + " << " + message_text)
    elif mesType == 1:
        print(getChatTemples(chat_id) + " >> " + message_text)
    elif mesType == 2:
        print(getChatTemples(chat_id) + " == " + message_text)
def getChatTemples(chat_id):
    return '[' +  str(chat_id) + ']'
def stopForDebug(individualStop, stop_text = ''):
    stopAll = True

    if stopAll or individualStop:
        input('!!! Остановка дебага: - ' + stop_text)
