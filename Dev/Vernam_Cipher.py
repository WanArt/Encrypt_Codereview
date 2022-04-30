from Find_In_Dict import get_symbol

# Символы в Коде Бодо для шифра Вернама
Bodo = dict(zip(['R', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '],
                ['01010', '00011', '11001', '01110', '01001', '00001', '01101', '11010', '10100', '00110',
                 '01011', '01111', '10010', '11100', '01100', '11000', '10110', '10111', '00101',
                 '10000', '00111', '11110', '10011', '11101', '10101', '10001', '00100']))


# Шифр Вернама
def Vernam_Cipher_Do(Message, KeyWord):
    """Шифр Вернама.

    Каждому символу из Message ставится
    в соответствие код Бодо из словаря.
    Выполняем операцию Код Бодо XOR Ключ(KeyWord).
    Получаем зашифрованное сообщение.

    """
    Ans: str = ''
    NewMessage: str = ''
    for i in Message:
        NewMessage += Bodo[i]
    k1 = 0
    k2 = 0
    NewKeyWord: str = ''
    while True:
        if k1 == len(KeyWord):
            k1 = 0
        NewKeyWord += KeyWord[k1]
        k1 += 1
        k2 += 1
        if len(NewMessage) == k2:
            break
    NewMessageList = list(NewMessage)
    for i in range(len(NewMessageList)):
        NewMessageList[i] = int(list(NewMessage)[i]) ^ int(list(NewKeyWord)[i])
    NewMessage = ''
    k1 = 0
    CipherList = []
    for i in range(len(NewMessageList)):
        NewMessageList[i] = str(NewMessageList[i])
    for i in range(len(NewMessageList)):
        NewMessage += NewMessageList[i]
        k1 += 1
        if k1 % 5 == 0:
            CipherList.append(NewMessage)
            NewMessage = ''
    length = len(CipherList)
    p = 0
    for i in range(length):
        try:
            Ans += get_symbol(Bodo, CipherList[i])
        except TypeError:
            p = 0
    return Ans


# Дешифровка шифра Вернама
def Vernam_Cipher_Undo(Message, KeyWord):
    """Дешифровка шифра Вернама.

        Аналогично шифру Вернама с тем же
        ключом, но Message - зашифрованное
        сообщение.

    """
    Ans: str = ''
    NewMessage: str = ''
    for i in Message:
        NewMessage += Bodo[i]
    k1 = 0
    k2 = 0
    NewKeyWord: str = ''
    while True:
        if k1 == len(KeyWord):
            k1 = 0
        NewKeyWord += KeyWord[k1]
        k1 += 1
        k2 += 1
        if len(NewMessage) == k2:
            break
    NewMessageList = list(NewMessage)
    for i in range(len(NewMessageList)):
        NewMessageList[i] = int(list(NewMessage)[i]) ^ int(list(NewKeyWord)[i])
    NewMessage = ''
    k1 = 0
    CipherList = []
    for i in range(len(NewMessageList)):
        NewMessageList[i] = str(NewMessageList[i])
    for i in range(len(NewMessageList)):
        NewMessage += NewMessageList[i]
        k1 += 1
        if k1 % 5 == 0:
            CipherList.append(NewMessage)
            NewMessage = ''
    p = 0
    for i in range(len(CipherList)):
        try:
            Ans += get_symbol(Bodo, CipherList[i])
        except TypeError:
            p = 0
    return Ans
