def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        data = file.read()
    encrypted_data = caesar_cipher(data, shift)
    with open(output_file, 'w') as file:
        file.write(encrypted_data)
    print("✅ File Encrypted Successfully!")


def decrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        data = file.read()
    decrypted_data = caesar_cipher(data, -shift)
    with open(output_file, 'w') as file:
        file.write(decrypted_data)
    print("✅ File Decrypted Successfully!")


# -------- Main Program --------
choice = input("Encrypt or Decrypt (E/D): ").upper()
input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")
shift = int(input("Enter shift key (number): "))

if choice == 'E':
    encrypt_file(input_file, output_file, shift)
elif choice == 'D':
    decrypt_file(input_file, output_file, shift)
else:
    print("❌ Invalid choice")
