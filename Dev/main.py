import pathlib
from pathlib import Path
import os
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
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
path3 = Path(pathlib.Path.cwd(), 'Files', 'Key.txt')
path_Alen_Cipher_Enc = Path(pathlib.Path.cwd(), 'Files', 'Alen_Cipher_Encrypt_Input.txt')
path_Alen_Cipher_Key = Path(pathlib.Path.cwd(), 'Files', 'Alen_Cipher_Key_Input.txt')
path_Bmp1 = Path(pathlib.Path.cwd(), 'Files', 'Bmp_Input.bmp')
path_Bmp2 = Path(pathlib.Path.cwd(), 'Files', 'Bmp-Output.bmp')
path_Key = Path(pathlib.Path.cwd(), 'Files', 'Keys.txt')
path_Fon = Path(pathlib.Path.cwd(), 'Files', 'Fon.jpg')


def encrypt_Caesar():
    file_input = open(path1)
    Tex = file_input.read()
    file_input.close()
    file_key = open(path3)
    GetKey = file_key.read()
    file_key.close()
    GetKey = int(GetKey)
    file_output = open(path2, 'w')
    file_output.write(Caesar_Cipher_Do(Tex, GetKey))
    file_output.close()


def encrypt_Vizhener():
    file_input = open(path1)
    Tex = file_input.read()
    file_input.close()
    file_key = open(path3)
    GetKey = file_key.read()
    file_key.close()
    file_output = open(path2, 'w')
    file_output.write(Vizhener_Cipher_Do(Tex.upper(), GetKey.upper()))
    file_output.close()


def encrypt_Vernam():
    file_input = open(path1)
    Tex = file_input.read()
    file_input.close()
    file_key = open(path3)
    GetKey = file_key.read()
    GetKey = int(GetKey)
    file_key.close()
    file_output = open(path2, 'w')
    file_output.write(Vernam_Cipher_Do(Tex.upper(), GetKey))
    file_output.close()


def encrypt_OneTimePad():
    file_input = open(path1)
    Tex = file_input.read()
    file_input.close()
    file_output = open(path2, 'w')
    file_output.write(One_Time_Pad_Cipher_Do(Tex))
    file_output.close()


def encrypt_Alen_Cipher():
    file_input = open(path1)
    Tex = file_input.read()
    file_input.close()
    file_output = open(path2, 'w')
    file_output.write(Alen_Cipher_Do(Tex))
    file_output.close()


def encrypt_Steganography():
    encode_image(path_Bmp1, path_Bmp2, path1, 8)


def decrypt_Caesar():
    file_input = open(path1)
    Tex = file_input.read()
    file_input.close()
    file_key = open(path3)
    GetKey = file_key.read()
    file_key.close()
    GetKey = int(GetKey)
    file_output = open(path2, 'w')
    file_output.write(Caesar_Cipher_Undo(Tex, GetKey))
    file_output.close()


def decrypt_Vizhener():
    file_input = open(path1)
    Tex = file_input.read()
    file_input.close()
    file_key = open(path3)
    GetKey = file_key.read()
    file_key.close()
    file_output = open(path2, 'w')
    file_output.write(Vizhener_Cipher_Undo(Tex.upper(), GetKey.upper()))
    file_output.close()


def decrypt_Vernam():
    file_input = open(path1)
    Tex = file_input.read()
    file_input.close()
    file_key = open(path3)
    GetKey = file_key.read()
    GetKey = int(GetKey)
    file_key.close()
    file_output = open(path2, 'w')
    file_output.write(Vernam_Cipher_Undo(Tex.upper(), GetKey))
    file_output.close()


def decrypt_OneTimePad():
    file_input = open(path1)
    Tex = file_input.read()
    file_input.close()
    file_output = open(path2, 'w')
    file_output.write(One_Time_Pad_Cipher_Undo(Tex))
    file_output.close()


def decrypt_Alen_Cipher():
    file_output = open(path2, 'w')
    List_E = pd.read_csv(path_Alen_Cipher_Enc, sep=" ", header=None)
    List_En = List_E.values.tolist()
    List_Enc = [item for sublist in List_En for item in sublist]
    List_K = pd.read_csv(path_Alen_Cipher_Key, sep=" ", header=None)
    List_Ke = List_K.values.tolist()
    List_Key = [item for sublist in List_Ke for item in sublist]
    file_output.write(Alen_Cipher_Undo(List_Enc, List_Key))
    file_output.close()


def decrypt_Steganography():
    Length_To_Read = os.stat(path1).st_size
    decode_image(path_Bmp2, path2, Length_To_Read, 8)


def hack():
    file_input = open(path1)
    Tex = file_input.read()
    file_input.close()
    file_output = open(path2, 'w')
    file_output.write(Freq_Hack(Tex))
    file_output.close()


root = Tk()
root.title("Encrypter")
root.geometry("650x300+200+100")
Label(root, text="Изменяйте входные данные", font=25, fg='white', bg='black').grid(row=0, column=0, sticky='w')
Label(root, text="    в папке Files", font=25, fg='white', bg='black').grid(row=1, column=0, sticky='w')
Label(root, text="            Шифрование", font=20, fg='white', bg='black').grid(row=2, column=0, sticky='w')
Label(root, text="Дешифрование", font=20, fg='white', bg='black').grid(row=2, column=1, sticky='w')
Label(root, text="           Взлом", font=20, fg='white', bg='black').grid(row=2, column=3, sticky='w')
root.configure(bg='black')
f1 = Frame(root)
f1.grid(row=3, column=0, sticky='nsew')
f2 = Frame(root)
f2.grid(row=3, column=1, sticky='nsew')
f3 = Frame(root)
f3.grid(row=3, column=3, sticky='nsew')
f4 = Frame(root)
f4.grid(row=4, column=0, sticky='nsew')
encryption_button1 = Button(f1, text="Шифр Цезаря", fg='white', bg='black', command=encrypt_Caesar)
encryption_button1.pack(side="top")
encryption_button2 = Button(f1, text="Шифр Виженера", fg='white', bg='black', command=encrypt_Vizhener)
encryption_button2.pack(side="top")
encryption_button3 = Button(f1, text="Шифр Вернама", fg='white', bg='black', command=encrypt_Vernam)
encryption_button3.pack(side="top")
encryption_button4 = Button(f1, text="Шифр OneTimePad", fg='white', bg='black', command=encrypt_OneTimePad)
encryption_button4.pack(side="top")
encryption_button5 = Button(f1, text="Шифр Алена", fg='white', bg='black', command=encrypt_Alen_Cipher)
encryption_button5.pack(side="top")
encryption_button6 = Button(f1, text="Шифр Стеганография", fg='white', bg='black', command=encrypt_Steganography)
encryption_button6.pack(side="top")
decryption_button1 = Button(f2, text="Шифр Цезаря", fg='white', bg='black', command=decrypt_Caesar)
decryption_button1.pack(side="top")
decryption_button2 = Button(f2, text="Шифр Виженера", fg='white', bg='black', command=decrypt_Vizhener)
decryption_button2.pack(side="top")
decryption_button3 = Button(f2, text="Шифр Вернама", fg='white', bg='black', command=decrypt_Vernam)
decryption_button3.pack(side="top")
decryption_button4 = Button(f2, text="Шифр OneTimePad", fg='white', bg='black', command=decrypt_OneTimePad)
decryption_button4.pack(side="top")
decryption_button5 = Button(f2, text="Шифр Алена", fg='white', bg='black', command=decrypt_Alen_Cipher)
decryption_button5.pack(side="top")
decryption_button6 = Button(f2, text="Шифр Стеганография", fg='white', bg='black', command=decrypt_Steganography)
decryption_button6.pack(side="top")
hack_button = Button(f3, text="Автоматический частотный взлом", fg='white', bg='black', command=hack)
hack_button.pack(side="top")
quit_button = Button(f1, text="Выйти", font=20, fg='white', bg='red', command=root.destroy)
quit_button.pack(side="top")
root.configure(bg='black')
root.mainloop()
