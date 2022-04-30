# Алфавиты для шифра Цезаря
Eng_Upper: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
Eng_Lower: str = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
Ru_Upper: str = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
Ru_Lower: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Шифр Цезаря
def Caesar_Cipher_Do(Message, Step):
    """Шифр Цезаря.

        Параметры функции:
            Message - сообщение для шифровки
            Step - шаг шифрования

        Каждый символ из Message сдвигается
        на шаг(Step) вправо. Получаем
        зашифрованое сообщение.

    """
    Ans: str = ''
    for i in Message:
        if i in Eng_Upper:
            Language: str = Eng_Upper
        elif i in Eng_Lower:
            Language: str = Eng_Lower
        elif i in Ru_Upper:
            Language: str = Ru_Upper
        else:
            Language: str = Ru_Lower
        Pos = Language.find(i) + Step
        if i not in Language:
            Ans += i
        else:
            Ans += Language[Pos]
    return Ans


# Дешифровка шифра Цезаря
def Caesar_Cipher_Undo(Message, Step):
    """Дешифровка шифра Цезаря.

        Параметры функции:
            Message - сообщение для дешифровки
            Step - шаг шифрования

        Аналогично шифру Цезаря,
        но сдвиг влево.

    """
    Ans: str = ''
    for i in Message:
        if i in Eng_Upper:
            Language: str = Eng_Upper
        elif i in Eng_Lower:
            Language: str = Eng_Lower
        elif i in Ru_Upper:
            Language: str = Ru_Upper
        else:
            Language: str = Ru_Lower
        Pos = Language.find(i) - Step
        if i not in Language:
            Ans += i
        else:
            Ans += Language[Pos]
    return Ans
