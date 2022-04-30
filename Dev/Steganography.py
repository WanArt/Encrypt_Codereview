import os
import sys

Size = 54


def encode_image(Input_Img_Name, Output_Img_Name, Message, Deg):
    """Шифр Стеганография.

        Параметры функции:
            Input_Img_Name - Первоначальное изображение
            Output_Img_Name - Зашифрованное изображение
            Message - сообщение для шифровки
            Deg - Ступень отступа


        Переводим Аски код символа
        в двоичную систему счисления
        и шифруем в стегоконтейнер,
        практисески не меняя цвет.
        Срезаем какое-то кол-во
        цифр из символа. Получаем
        загифрованное bmp-изображение

    """
    if Deg not in [1, 2, 4, 8]:
        return False
    Text_len = os.stat(Message).st_size
    Img_len = os.stat(Input_Img_Name).st_size
    if Text_len >= Img_len * Deg / 8 - Size:
        return False
    Text = open(Message, 'r')
    Input_image = open(Input_Img_Name, 'rb')
    Output_image = open(Output_Img_Name, 'wb')
    Bmp_header = Input_image.read(Size)
    Output_image.write(Bmp_header)
    Text_mask, Img_mask = create_masks(Deg)
    while True:
        Symbol = Text.read(1)
        if not Symbol:
            break
        Symbol = ord(Symbol)
        for Byte_amount in range(0, 8, Deg):
            Img_byte = int.from_bytes(Input_image.read(1), sys.byteorder) & Img_mask
            Bits = Symbol & Text_mask
            Bits >>= (8 - Deg)
            Img_byte |= Bits
            Output_image.write(Img_byte.to_bytes(1, sys.byteorder))
            Symbol <<= Deg
    Output_image.write(Input_image.read())
    Text.close()
    Input_image.close()
    Output_image.close()
    return True


def decode_image(Encoded_img, Output_txt, Symbols_to_read, Deg):
    """Дешифровка шифра Стеганография.

        Параметры функции:
            Encoded_img - Зашифорванное изображение
            Output_txt - Дешифрованное сообщение
            Symbols_to_read - Размер сообщения
            Deg - Ступень отступа

        Аналогично, в обратную сторону.

    """
    if Deg not in [1, 2, 4, 8]:
        return False
    Img_len = os.stat(Encoded_img).st_size
    if Symbols_to_read >= Img_len * Deg / 8 - Size:
        return False
    Text = open(Output_txt, 'w', encoding='utf-8')
    Encoded_bmp = open(Encoded_img, 'rb')
    Encoded_bmp.seek(Size)
    _, Img_mask = create_masks(Deg)
    Img_mask = ~Img_mask
    Read = 0
    while Read < Symbols_to_read:
        Symbol = 0
        for Bits_read in range(0, 8, Deg):
            Img_byte = int.from_bytes(Encoded_bmp.read(1), sys.byteorder) & Img_mask
            Symbol <<= Deg
            Symbol |= Img_byte
        if chr(Symbol) == '\n' and len(os.linesep) == 2:
            Read += 1
        Read += 1
        Text.write(chr(Symbol))
    Text.close()
    Encoded_bmp.close()
    return True


def create_masks(degree):
    Text_mask = 0b11111111
    Img_mask = 0b11111111
    Text_mask <<= (8 - degree)
    Text_mask %= 256
    Img_mask >>= degree
    Img_mask <<= degree
    return Text_mask, Img_mask
