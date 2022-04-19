from random import randint
from Find_In_Dict import get_symbol

# Шифр Алена
Dict_Alen = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '],
                     [1010101, 2020202, 3030303, 4040404, 5050505, 6060606, 7070707, 8080808, 9090909, 10101010,
                      11111111, 12121212, 13131313, 14141414, 15151515, 16161616, 17171717, 18181818, 19191919,
                      20202020, 21212121, 22222222, 23232323, 24242424, 25252525, 26262626, 27272727]))


# Шифр Алена
def Alen_Cipher_Do(Message):
    Key_List: list = []
    Str_Key_List: str = ''
    Enc_List: list = []
    Str_Enc_List: str = ''
    Str_Output: str = ''

    def Generate_Key():
        return randint(100_000_000, 999_999_999)

    for i in range(len(Message)):
        Current_Key = 0
        Symbol = Message[i]
        Symbol_Val = Dict_Alen[Symbol]
        Current_Key = Generate_Key()
        Symbol_Val += Current_Key
        Key_List.append(Current_Key)
        Enc_List.append(Symbol_Val)
    for j in range(len(Enc_List)):
        Str_Enc_List += str(Enc_List[j])
        Str_Enc_List += ' '
    for j in range(len(Enc_List)):
        Str_Output += Str_Enc_List
    for q in range(len(Key_List)):
        Str_Key_List += str(Key_List[q])
        Str_Key_List += ' '
    Str_Output += '\n'
    for q in range(len(Key_List)):
        Str_Output += Str_Key_List
    return Str_Output


# Дешифровка шифра Алена
def Alen_Cipher_Undo(Enc_List: list, Key_List: list):
    Dec_List: list = []
    Message: str = ''
    Message_Len: int = 0
    for i in range(len(Enc_List)):
        Dec_List.append(Enc_List[i] - Key_List[i])
    SQRT = len(Dec_List) ** 0.5
    for i in range(len(Dec_List)):
        Dec_List[i] = get_symbol(Dict_Alen, Dec_List[i])
        Message += Dec_List[i]
    return Message[:int(SQRT)]
