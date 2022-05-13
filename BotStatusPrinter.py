def printStatusBot(message_data, chat_id, message_text, mesType):
    if mesType == 0:
        print(getChatTemples(chat_id) + " << " + message_text)
    elif mesType == 1:
        print(getChatTemples(chat_id) + " >> " + message_text)
    elif mesType == 2:
        print(getChatTemples(chat_id) + " == " + message_text)
def getChatTemples(chat_id):
    return '[' +  str(chat_id) + ']'

#Функция для остановки дебага или просто остановки. Останавливает индивидуально строку,
    #или же все строки при инциализации дебага в начале
stopAll = int(input("Режим дебага? Введите 1 (да) или 0 (нет):\n"))
def stopForDebug(individualStop, stop_text = ''):

    if stopAll == 1 or individualStop == 1:
        input('!!! Остановка дебага: - ' + stop_text)
