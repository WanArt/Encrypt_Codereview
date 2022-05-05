from Src.Caesar_Cipher import Caesar_Cipher_Do, Caesar_Cipher_Undo
from Src.Globals import GlobalsVar as Gv


# Шифр Виженера
def Vizhener_Cipher_Do(Message, KeyWord):
    """Шифр Виженера.

        Параметры функции:
            Message - сообщение для шифровки
            KeyWord - ключ для шифровки

        Символы ключа(KeyWord) дублируются,
        пока его длина не совпадет с длиной
        Message. Затем в матрице вида
        алфавит х алфавит ищем пересечение
        символа KeyWord <-> символа Message,
        получая зашифрованное сообщение.

    """
    Ans: str = ''
    NewKeyWord: str = ''
    k1 = 0
    k2 = 0
    while True:
        if k1 == len(KeyWord):
            k1 = 0
        NewKeyWord += KeyWord[k1]
        k1 += 1
        k2 += 1
        if len(Message) == k2:
            break
    Key = [ord(char) - Gv.Shift for char in NewKeyWord.lower()]

    num_of_iterations = len(Key)

    for i in range(num_of_iterations):
        Key[i] -= 1

    num_of_iterations = len(NewKeyWord)

    for i in range(num_of_iterations):
        Ans += Caesar_Cipher_Do(Message[i], Key[i])
    return Ans


# Дешифровка шифра Виженера
def Vizhener_Cipher_Undo(Message, KeyWord):
    """Дешифровка шифра Виженера.

        Параметры функции:
            Message - сообщение для дешифровки
            KeyWord - ключ для дешифровки

        Аналогично шифру Виженера с тем же
        ключом, но Message - зашифрованное
        сообщение.

    """
    Ans: str = ''
    NewKeyWord: str = ''
    k1 = 0
    k2 = 0
    while True:
        if k1 == len(KeyWord):
            k1 = 0
        NewKeyWord += KeyWord[k1]
        k1 += 1
        k2 += 1
        if len(Message) == k2:
            break
    Key = [ord(char) - Gv.Shift for char in NewKeyWord.lower()]

    num_of_iterations = len(Key)

    for i in range(num_of_iterations):
        Key[i] -= 1

    num_of_iterations = len(NewKeyWord)

    for i in range(num_of_iterations):
        Ans += Caesar_Cipher_Undo(Message[i], Key[i])
    return Ans
