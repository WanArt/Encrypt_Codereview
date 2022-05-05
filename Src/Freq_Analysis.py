import math
from collections import Counter
from Src.Caesar_Cipher import Caesar_Cipher_Undo
from Src.Globals import GlobalsVar as Gv


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
    Len_Alph: int = len(Gv.Eng_Lower)
    Undo_Step = 0

    def Contrast(Str):
        Cnt = Counter(Str)
        Alph = Gv.Eng_Lower
        Alph_Length = len(Gv.Eng_Lower)
        Ans_Full = sum([
            abs(Cnt.get(Text, 0) * Gv.Contrast_Size / len(Str) - Gv.Freq[Text])
            for Text in Alph])
        Ans_Point = Ans_Full / Alph_Length
        return Ans_Point

    def Caesar_Test(Str, Key_Word, Dec):
        Current: str = ''
        for Symbol in Str:
            if Symbol not in Gv.Eng_Lower:
                Current += Symbol
                continue
            Ind = Gv.Eng_Lower.index(Symbol.lower())
            if not Dec:
                Symbol_Last = Gv.Eng_Lower[(Ind + Key_Word) % len(Gv.Eng_Lower)]
            else:
                Symbol_Last = Gv.Eng_Lower[(Ind - Key_Word) % len(Gv.Eng_Lower)]
            Current += Symbol_Last.upper() if Symbol.isupper() else Symbol_Last
        return Current

    for Step in range(1, Len_Alph):
        current_plain_text = Caesar_Test(Message, Step, True)
        Con = Contrast(current_plain_text)
        if Low_Con > Con:
            Low_Con = Con
            Undo_Step = Step
    return Caesar_Cipher_Undo(Message, Undo_Step)
