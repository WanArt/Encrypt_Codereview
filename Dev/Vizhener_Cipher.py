from Caesar_Cipher import Caesar_Cipher_Do, Caesar_Cipher_Undo


# Шифр Виженера
def Vizhener_Cipher_Do(Message, KeyWord):
    """Шифр Виженера.

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
    Key = [ord(char) - 96 for char in NewKeyWord.lower()]
    for i in range(len(Key)):
        Key[i] -= 1
    for i in range(len(NewKeyWord)):
        Ans += Caesar_Cipher_Do(Message[i], Key[i])
    return Ans


# Дешифровка шифра Виженера
def Vizhener_Cipher_Undo(Message, KeyWord):
    """Дешифровка шифра Виженера.

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
    Key = [ord(char) - 96 for char in NewKeyWord.lower()]
    for i in range(len(Key)):
        Key[i] -= 1
    for i in range(len(NewKeyWord)):
        Ans += Caesar_Cipher_Undo(Message[i], Key[i])
    return Ans
