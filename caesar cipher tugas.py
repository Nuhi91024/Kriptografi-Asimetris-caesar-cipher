# Fungsi untuk mengenkripsi pesan menggunakan Caesar Cipher
def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    
    # Iterasi melalui setiap karakter di plaintext
    for char in plaintext:
        # Memeriksa apakah karakter adalah huruf
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            # Menggeser posisi karakter sesuai dengan shift
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Jika bukan huruf, tetap menggunakan karakter asli
            encrypted_text += char
    
    return encrypted_text

# Fungsi untuk mendekripsi pesan menggunakan Caesar Cipher
def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    
    # Iterasi melalui setiap karakter di ciphertext
    for char in ciphertext:
        # Memeriksa apakah karakter adalah huruf
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            # Menggeser posisi karakter kembali sesuai dengan shift
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            # Jika bukan huruf, tetap menggunakan karakter asli
            decrypted_text += char
    
    return decrypted_text

# Contoh penggunaan
plaintext = "Nurhidayati!"
shift = 5

# Enkripsi pesan
encrypted_message = encrypt_caesar(plaintext, shift)
print(f"Pesan terenkripsi: {encrypted_message}")

# Dekripsi pesan
decrypted_message = decrypt_caesar(encrypted_message, shift)
print(f"Pesan terdekripsi: {decrypted_message}")
