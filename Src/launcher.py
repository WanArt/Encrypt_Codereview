import pathlib
from pathlib import Path
import os
import pandas as pd
import tkinter as tk
from PIL import ImageTk, Image
from Src.Caesar_Cipher import Caesar_Cipher_Do, Caesar_Cipher_Undo
from Src.Vizhener_Cipher import Vizhener_Cipher_Do, Vizhener_Cipher_Undo
from Src.Vernam_Cipher import Vernam_Cipher_Undo, Vernam_Cipher_Do
from Src.Freq_Analysis import Freq_Hack
from Src.Alen_Cipher import Alen_Cipher_Do, Alen_Cipher_Undo
from Src.OneTimePad_Cipher import One_Time_Pad_Cipher_Do, One_Time_Pad_Cipher_Undo
from Src.Steganography import encode_image, decode_image
from Src.Globals import GlobalsVar as Gv


# Класс сборки программы для запуска
class Launch:
    @staticmethod
    def start():
        # Путь к файлу
        dir_path = pathlib.Path.cwd()
        path1 = Path(pathlib.Path.cwd(), 'Examples', 'Input.txt')
        path2 = Path(pathlib.Path.cwd(), 'Examples', 'Output.txt')
        path3 = Path(pathlib.Path.cwd(), 'Examples', 'Keys.txt')
        path_Alen_Cipher_Enc = Path(pathlib.Path.cwd(), 'Examples',
                                    'Alen_Cipher_Encrypt_Input.txt')
        path_Alen_Cipher_Key = Path(pathlib.Path.cwd(), 'Examples',
                                    'Alen_Cipher_Key_Input.txt')
        path_Bmp1 = Path(pathlib.Path.cwd(), 'Examples', 'Bmp_Input.bmp')
        path_Bmp2 = Path(pathlib.Path.cwd(), 'Examples', 'Bmp-Output.bmp')

        # path_Key = Path(pathlib.Path.cwd(), 'Files', 'Keys.txt')
        # path_Fon = Path(pathlib.Path.cwd(), 'Files', 'Fon.jpg')

        def encrypt_Caesar():
            """Шифрование методом Цезаря с аргументами из файла"""
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
            """Шифрование методом Виженера с аргументами из файла"""
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
            """Шифрование методом Вернама с аргументами из файла"""
            file_input = open(path1)
            Tex = file_input.read()
            file_input.close()
            file_key = open(path3)
            GetKey = file_key.read()
            file_key.close()
            file_output = open(path2, 'w')
            file_output.write(Vernam_Cipher_Do(Tex.upper(), GetKey))
            file_output.close()

        def encrypt_OneTimePad():
            """Шифрование методом OneTimePad с аргументами из файла"""
            file_input = open(path1)
            Tex = file_input.read()
            file_input.close()
            file_output = open(path2, 'w')
            file_output.write(One_Time_Pad_Cipher_Do(Tex))
            file_output.close()

        def encrypt_Alen_Cipher():
            """Шифрование методом Алена с аргументами из файла"""
            file_input = open(path1)
            Tex = file_input.read()
            file_input.close()
            file_output = open(path2, 'w')
            file_output.write(Alen_Cipher_Do(Tex))
            file_output.close()

        def encrypt_Steganography():
            """Шифрование методом Стеганография с аргументами из файла"""
            encode_image(path_Bmp1, path_Bmp2, path1, 8)

        def decrypt_Caesar():
            """Дешифровка методом Цезаря с аргументами из файла"""
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
            """Дешифровка методом Виженера с аргументами из файла"""
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
            """Дешифровка методом Вернама с аргументами из файла"""
            file_input = open(path1)
            Tex = file_input.read()
            file_input.close()
            file_key = open(path3)
            GetKey = file_key.read()
            file_key.close()
            file_output = open(path2, 'w')
            file_output.write(Vernam_Cipher_Undo(Tex.upper(), GetKey))
            file_output.close()

        def decrypt_OneTimePad():
            """Дешифровка методом OneTimePad с аргументами из файла"""
            file_input = open(path1)
            Tex = file_input.read()
            file_input.close()
            file_output = open(path2, 'w')
            file_output.write(One_Time_Pad_Cipher_Undo(Tex))
            file_output.close()

        def decrypt_Alen_Cipher():
            """Дешифровка методом Алена с аргументами из файла"""
            file_output = open(path2, 'w')
            List_Enc_Path = pd.read_csv(path_Alen_Cipher_Enc, sep=" ", header=None)
            List_Enc_To_List = List_Enc_Path.values.tolist()
            List_Enc = [item for sublist in List_Enc_To_List for item in sublist]
            List_Key_Path = pd.read_csv(path_Alen_Cipher_Key, sep=" ", header=None)
            List_Key_To_List = List_Key_Path.values.tolist()
            List_Key = [item for sublist in List_Key_To_List for item in sublist]
            file_output.write(Alen_Cipher_Undo(List_Enc, List_Key))
            file_output.close()

        def decrypt_Steganography():
            """Дешифровка методом Стеганография с аргументами из файла"""
            Length_To_Read = os.stat(path1).st_size
            decode_image(path_Bmp2, path2, Length_To_Read, 8)

        def hack():
            """Дешифровка методом частотного взлома с аргументами из файла"""
            file_input = open(path1)
            Tex = file_input.read()
            file_input.close()
            file_output = open(path2, 'w')
            file_output.write(Freq_Hack(Tex))
            file_output.close()

        """Графический интерфейс"""
        root = tk.Tk()
        root.title("Encrypter")
        root.geometry("650x300+200+100")
        tk.Label(root, text="Изменяйте входные данные", font=Gv.Font_Size_25, fg='black', bg='yellow').grid(row=0,
                                                                                                            column=0,
                                                                                                            sticky='w')
        tk.Label(root, text="    в папке Files", font=Gv.Font_Size_25, fg='black', bg='yellow').grid(row=Gv.Row_Size_1,
                                                                                                     column=0,
                                                                                                     sticky='w')
        tk.Label(root, text="            Шифрование", font=Gv.Font_Size_20, fg='black', bg='white').grid(
            row=Gv.Row_Size_2,
            column=0,
            sticky='w')
        tk.Label(root, text="Дешифрование", font=Gv.Font_Size_20, fg='black', bg='white').grid(row=Gv.Row_Size_2,
                                                                                               column=Gv.Column_Size_1,
                                                                                               sticky='w')
        tk.Label(root, text="           Взлом", font=Gv.Font_Size_20, fg='black', bg='white').grid(
            row=Gv.Row_Size_2,
            column=Gv.Column_Size_3,
            sticky='w')
        root.configure(bg='black')
        f1 = tk.Frame(root)
        f1.grid(row=Gv.Row_Size_3, column=0, sticky='nsew')
        f2 = tk.Frame(root)
        f2.grid(row=Gv.Row_Size_3, column=Gv.Column_Size_1, sticky='nsew')
        f3 = tk.Frame(root)
        f3.grid(row=Gv.Row_Size_3, column=Gv.Column_Size_3, sticky='nsew')
        f4 = tk.Frame(root)
        f4.grid(row=Gv.Row_Size_4, column=0, sticky='nsew')
        encryption_button1 = tk.Button(f1, text="Шифр Цезаря", fg='white', bg='gray', command=encrypt_Caesar)
        encryption_button1.pack(side="top")
        encryption_button2 = tk.Button(f1, text="Шифр Виженера", fg='white', bg='gray', command=encrypt_Vizhener)
        encryption_button2.pack(side="top")
        encryption_button3 = tk.Button(f1, text="Шифр Вернама", fg='white', bg='gray', command=encrypt_Vernam)
        encryption_button3.pack(side="top")
        encryption_button4 = tk.Button(f1, text="Шифр OneTimePad", fg='white', bg='gray', command=encrypt_OneTimePad)
        encryption_button4.pack(side="top")
        encryption_button5 = tk.Button(f1, text="Шифр Алена", fg='white', bg='gray', command=encrypt_Alen_Cipher)
        encryption_button5.pack(side="top")
        encryption_button6 = tk.Button(f1, text="Шифр Стеганография", fg='white', bg='gray',
                                       command=encrypt_Steganography)
        encryption_button6.pack(side="top")
        decryption_button1 = tk.Button(f2, text="Шифр Цезаря", fg='white', bg='gray', command=decrypt_Caesar)
        decryption_button1.pack(side="top")
        decryption_button2 = tk.Button(f2, text="Шифр Виженера", fg='white', bg='gray', command=decrypt_Vizhener)
        decryption_button2.pack(side="top")
        decryption_button3 = tk.Button(f2, text="Шифр Вернама", fg='white', bg='gray', command=decrypt_Vernam)
        decryption_button3.pack(side="top")
        decryption_button4 = tk.Button(f2, text="Шифр OneTimePad", fg='white', bg='gray', command=decrypt_OneTimePad)
        decryption_button4.pack(side="top")
        decryption_button5 = tk.Button(f2, text="Шифр Алена", fg='white', bg='gray', command=decrypt_Alen_Cipher)
        decryption_button5.pack(side="top")
        decryption_button6 = tk.Button(f2, text="Шифр Стеганография", fg='white', bg='gray',
                                       command=decrypt_Steganography)
        decryption_button6.pack(side="top")
        hack_button = tk.Button(f3, text="Автоматический частотный взлом", fg='white', bg='gray', command=hack)
        hack_button.pack(side="top")
        quit_button = tk.Button(f1, text="Выйти", font=Gv.Font_Size_20, fg='white', bg='red', command=root.destroy)
        quit_button.pack(side="top")
        root.configure(bg='white')
        root.mainloop()
