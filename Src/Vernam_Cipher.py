from Globals import GlobalsVar as Gv


# Получить ключ по значению
def get_symbol(sl, val):
    """Фукнция находит аргумент словаря по ключу

        Параметры функции:
            sl - словарь
            val - значение ключа

    """
    for a, b in sl.items():
        if val == b:
            return a


# Шифр Вернама
def Vernam_Cipher_Do(Message, KeyWord):
    """Шифр Вернама.

        Параметры функции:
            Message - сообщение для шифровки
            KeyWord - ключ для шифровки

        Каждому символу из Message ставится
        в соответствие код Бодо из словаря.
        Выполняем операцию Код Бодо XOR Ключ(KeyWord).
        Получаем зашифрованное сообщение.

    """
    Ans: str = ''
    NewMessage: str = ''
    for i in Message:
        NewMessage += Gv.Bodo[i]
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

    num_of_iterations = len(NewMessageList)

    for i in range(num_of_iterations):
        NewMessageList[i] = int(list(NewMessage)[i]) ^ int(list(NewKeyWord)[i])
    NewMessage = ''
    k1 = 0
    CipherList = []

    num_of_iterations = len(NewMessageList)

    for i in range(num_of_iterations):
        NewMessageList[i] = str(NewMessageList[i])

    num_of_iterations = len(NewMessageList)

    for i in range(num_of_iterations):
        NewMessage += NewMessageList[i]
        k1 += 1
        if k1 % Gv.Size_Condition == 0:
            CipherList.append(NewMessage)
            NewMessage = ''
    length = len(CipherList)
    p = 0
    for i in range(length):
        try:
            Ans += get_symbol(Gv.Bodo, CipherList[i])
        except TypeError:
            p = 0
    return Ans


# Дешифровка шифра Вернама
def Vernam_Cipher_Undo(Message, KeyWord):
    """Дешифровка шифра Вернама.

        Параметры функции:
            Message - сообщение для дешифровки
            KeyWord - ключ для дешифровки

        Аналогично шифру Вернама с тем же
        ключом, но Message - зашифрованное
        сообщение.

    """
    Ans: str = ''
    NewMessage: str = ''
    for i in Message:
        NewMessage += Gv.Bodo[i]
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

    num_of_iterations = len(NewMessageList)

    for i in range(num_of_iterations):
        NewMessageList[i] = int(list(NewMessage)[i]) ^ int(list(NewKeyWord)[i])
    NewMessage = ''
    k1 = 0
    CipherList = []

    num_of_iterations = len(NewMessageList)

    for i in range(num_of_iterations):
        NewMessageList[i] = str(NewMessageList[i])

    num_of_iterations = len(NewMessageList)

    for i in range(num_of_iterations):
        NewMessage += NewMessageList[i]
        k1 += 1
        if k1 % Gv.Size_Condition == 0:
            CipherList.append(NewMessage)
            NewMessage = ''
    p = 0

    num_of_iterations = len(CipherList)

    for i in range(num_of_iterations):
        try:
            Ans += get_symbol(Gv.Bodo, CipherList[i])
        except TypeError:
            p = 0
    return Ans
