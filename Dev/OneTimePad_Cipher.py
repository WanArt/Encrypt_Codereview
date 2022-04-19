import onetimepad


def One_Time_Pad_Cipher_Do(Message):
    return onetimepad.encrypt(Message, 'random')


def One_Time_Pad_Cipher_Undo(Message):
    return onetimepad.decrypt(Message, 'random')
