import onetimepad


def One_Time_Pad_Cipher_Do(Message):
    """Шифр OneTimePad.

            Используется библиотека onetimepad.
            Более сложный вариант шифра Вернама.

    """
    return onetimepad.encrypt(Message, 'random')


def One_Time_Pad_Cipher_Undo(Message):
    """Дешифровка шифра OneTimePad.

                Используется библиотека onetimepad.

    """
    return onetimepad.decrypt(Message, 'random')
