from random import randint
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


# Шифр Алена
def Alen_Cipher_Do(Message):
    """Шифр Алена.

        Параметры функции:
            Message - текст для шифровки

        Каждому символу ставится в соответствие
        8значное число из словаря.
        К каждому символу прибавляется рандомно
        сгенерированный ключ, получая новый символ.
        На выходе получается файл с зашифрованным
        сообщением и массив ключей

    """
    Key_List: list = []
    Str_Key_List: str = ''
    Enc_List: list = []
    Str_Enc_List: str = ''
    Str_Output: str = ''

    def Generate_Key():
        return randint(100_000_000, 999_999_999)

    num_of_iterations = len(Message)

    for i in range(num_of_iterations):
        Current_Key = 0
        Symbol = Message[i]
        Symbol_Val = Gv.Dict_Alen[Symbol]
        Current_Key = Generate_Key()
        Symbol_Val += Current_Key
        Key_List.append(Current_Key)
        Enc_List.append(Symbol_Val)

    num_of_iterations = len(Enc_List)

    for j in range(num_of_iterations):
        Str_Enc_List += str(Enc_List[j])
        Str_Enc_List += ' '

    num_of_iterations = len(Enc_List)

    for j in range(num_of_iterations):
        Str_Output += Str_Enc_List

    num_of_iterations = len(Key_List)

    for q in range(num_of_iterations):
        Str_Key_List += str(Key_List[q])
        Str_Key_List += ' '
    Str_Output += '\n'

    num_of_iterations = len(Key_List)

    for q in range(num_of_iterations):
        Str_Output += Str_Key_List
    return Str_Output


# Дешифровка шифра Алена
def Alen_Cipher_Undo(Enc_List: list, Key_List: list):
    """Дешифровка шифра Алена

        Параметры функции:
            Enc_List - зашифрованное сообщение
            Key_List - массив ключей шифрования

        Аналогично шифрованию, надо
        знать словарь, массив ключей и
        зашифрованное сообщение

    """
    Dec_List: list = []
    Message: str = ''
    Message_Len: int = 0

    num_of_iterations = len(Enc_List)

    for i in range(num_of_iterations):
        Dec_List.append(Enc_List[i] - Key_List[i])
    SQRT = len(Dec_List) ** Gv.SQRT

    num_of_iterations = len(Dec_List)

    for i in range(num_of_iterations):
        Dec_List[i] = get_symbol(Gv.Dict_Alen, Dec_List[i])
        Message += Dec_List[i]
    return Message[:int(SQRT)]
