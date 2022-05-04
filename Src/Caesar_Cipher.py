from Globals import GlobalsVar as Gv


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
        if i in Gv.Eng_Upper:
            Language: str = Gv.Eng_Upper
        elif i in Gv.Eng_Lower:
            Language: str = Gv.Eng_Lower
        elif i in Gv.Ru_Upper:
            Language: str = Gv.Ru_Upper
        else:
            Language: str = Gv.Ru_Lower
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
        if i in Gv.Eng_Upper:
            Language: str = Gv.Eng_Upper
        elif i in Gv.Eng_Lower:
            Language: str = Gv.Eng_Lower
        elif i in Gv.Ru_Upper:
            Language: str = Gv.Ru_Upper
        else:
            Language: str = Gv.Ru_Lower
        Pos = Language.find(i) - Step
        if i not in Language:
            Ans += i
        else:
            Ans += Language[Pos]
    return Ans
