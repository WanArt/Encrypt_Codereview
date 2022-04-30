import math
from collections import Counter
from Caesar_Cipher import Caesar_Cipher_Undo

# Алфавиты для шифра Цезаря
Eng_Upper: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
Eng_Lower: str = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
Ru_Upper: str = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
Ru_Lower: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Частота
Freq = {'e': 12.7, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
        'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
        'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
        'q': 0.10, 'z': 0.07}


# Частотный анализ
def Freq_Hack(Message):
    """Взлом сообщения методом частотного анализа.

        Параметры функции:
            Message - сообщение для взлома

        Алгоритм уже знает частоту встречающегося символа
        в языке. В большом тексте меняет зашифрованный символ
        на подходящий по частоте

    """
    Low_Con = math.inf
    Len_Alph: int = len(Eng_Lower)
    Undo_Step = 0

    def Contrast(Str):
        Cnt = Counter(Str)
        return sum(
            [abs(Cnt.get(Text, 0) * 100 / len(Str) - Freq[Text]) for Text in Eng_Lower]) / len(
            Eng_Lower)

    def Caesar_Test(Str, Key_Word, Dec):
        Current: str = ''
        for Symbol in Str:
            if Symbol not in Eng_Lower:
                Current += Symbol
                continue
            Ind = Eng_Lower.index(Symbol.lower())
            if not Dec:
                Symbol_Last = Eng_Lower[(Ind + Key_Word) % len(Eng_Lower)]
            else:
                Symbol_Last = Eng_Lower[(Ind - Key_Word) % len(Eng_Lower)]
            Current += Symbol_Last.upper() if Symbol.isupper() else Symbol_Last
        return Current

    for Step in range(1, Len_Alph):
        current_plain_text = Caesar_Test(Message, Step, True)
        Con = Contrast(current_plain_text)
        if Low_Con > Con:
            Low_Con = Con
            Undo_Step = Step
    return Caesar_Cipher_Undo(Message, Undo_Step)
