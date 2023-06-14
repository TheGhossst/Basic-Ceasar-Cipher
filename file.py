def encrypt(text, key):
    """
    Encrypts the input text using the provided key.
    """
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + ord(key))
    return encrypted

def decrypt(text, key):
    """
    Decrypts the input text using the provided key.
    """
    decrypted = ""
    for char in text:
        decrypted += chr(ord(char) - ord(key))
    return decrypted

def file_encrypt_decrypt():
    filename = input("Enter the name of the text file you want to encrypt or decrypt: ")  
    key = input("Enter an encryption key (a single character): ")  
    operation = input("Do you want to encrypt or decrypt the file? (E/D): ")
    with open(filename, 'r') as file:
        text = file.read()
    if operation == 'E':
        result = encrypt(text, key)
        output_filename = filename.split('.')[0] + '_encrypted.txt'
    elif operation == 'D':
        result = decrypt(text, key)
        output_filename = filename.split('.')[0] + '_decrypted.txt'
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")
        return
    with open(output_filename, 'w') as file:
        file.write(result)
    print(f"File '{filename}' {operation.lower()}ed successfully as '{output_filename}'.")
file_encrypt_decrypt()