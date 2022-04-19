import pathlib
from pathlib import Path
import os
import pandas as pd
from Caesar_Cipher import Caesar_Cipher_Do, Caesar_Cipher_Undo
from Vizhener_Cipher import Vizhener_Cipher_Do, Vizhener_Cipher_Undo
from Vernam_Cipher import Vernam_Cipher_Undo, Vernam_Cipher_Do
from Freq_Analysis import Freq_Hack
from Alen_Cipher import Alen_Cipher_Do, Alen_Cipher_Undo
from OneTimePad_Cipher import One_Time_Pad_Cipher_Do, One_Time_Pad_Cipher_Undo
from Steganography import encode_image, decode_image

# Путь к файлу
dir_path = pathlib.Path.cwd()
path1 = Path(pathlib.Path.cwd(), 'Files', 'Input.txt')
path2 = Path(pathlib.Path.cwd(), 'Files', 'Output.txt')
path_Alen_Cipher_Enc = Path(pathlib.Path.cwd(), 'Files', 'Alen_Cipher_Encrypt_Input.txt')
path_Alen_Cipher_Key = Path(pathlib.Path.cwd(), 'Files', 'Alen_Cipher_Key_Input.txt')
path_Bmp1 = Path(pathlib.Path.cwd(), 'Files', 'Bmp_Input.bmp')
path_Bmp2 = Path(pathlib.Path.cwd(), 'Files', 'Bmp-Output.bmp')
path_Key = Path(pathlib.Path.cwd(), 'Files', 'Keys.txt')

# Чтение из файла
file_input = open(path1)
Text = file_input.read()
file_input.close()

file_output = open(path2, 'w')

print("Зашифровать - 1, Дешифровать - 2, Взломать - 3")
Method = int(input())
if Method == 1:
    print("Выберите метод шифрования(1, 2, 3): Шифр Цезаря - 1, Шифр Виженера - 2, Шифр Вернама - 3, "
          "Шифр OneTimePad - 4, Шифр Алена = 5, Стеганография - 6")
    Method_Do = int(input())
    if Method_Do == 1:
        print("Введите шаг: ")
        GetKey = int(input())
        file_output.write(Caesar_Cipher_Do(Text, GetKey))
    if Method_Do == 2:
        print("Введите ключ: ")
        GetKey = str(input())
        file_output.write(Vizhener_Cipher_Do(Text.upper(), GetKey.upper()))
    if Method_Do == 3:
        print("Введите ключ(двоичное число пяти разрядов): ")
        GetKey = str(input())
        file_output.write(Vernam_Cipher_Do(Text.upper(), GetKey))
    if Method_Do == 4:
        file_output.write(One_Time_Pad_Cipher_Do(Text))
    if Method_Do == 5:
        file_output.write(Alen_Cipher_Do(Text.lower()))
    if Method_Do == 6:
        encode_image(path_Bmp1, path_Bmp2, path1, 8)
if Method == 2:
    print("Что нужно дешифровать(1, 2, 3): Шифр Цезаря - 1, Шифр Виженера - 2, Шифр Вернама - 3, Шифр OneTimePad - 4, "
          "Шифр Алена - 5, Стеганогафия - 6")
    Method_Undo = int(input())
    if Method_Undo == 1:
        print("Введите шаг: ")
        GetKey = int(input())
        file_output.write(Caesar_Cipher_Undo(Text, GetKey))
    if Method_Undo == 2:
        print("Введите ключ: ")
        GetKey = str(input())
        file_output.write(Vizhener_Cipher_Undo(Text.upper(), GetKey.upper()))
    if Method_Undo == 3:
        print("Введите  ключ: ")
        GetKey = str(input())
        file_output.write(Vernam_Cipher_Undo(Text.upper(), GetKey))
    if Method_Undo == 4:
        file_output.write(One_Time_Pad_Cipher_Undo(Text))
    if Method_Undo == 5:
        List_E = pd.read_csv(path_Alen_Cipher_Enc, sep=" ", header=None)
        List_En = List_E.values.tolist()
        List_Enc = [item for sublist in List_En for item in sublist]
        List_K = pd.read_csv(path_Alen_Cipher_Key, sep=" ", header=None)
        List_Ke = List_K.values.tolist()
        List_Key = [item for sublist in List_Ke for item in sublist]
        file_output.write(Alen_Cipher_Undo(List_Enc, List_Key))
    if Method_Undo == 6:
        Length_To_Read = os.stat(path1).st_size
        decode_image(path_Bmp2, path2, Length_To_Read, 8)
if Method == 3:
    file_output.write(Freq_Hack(Text))

file_output.close()
