import os
import random
import secrets
from typing import Optional


def generate_random_key_file(key_path: str, size: int, method: str = "urandom"):
    "Задача 1: Генерация файла-ключа"
    print(f"Генерация ключа ({size} байт) методом: {method}")
    
    if method == "urandom":
        key = secrets.token_bytes(size)          
    elif method == "random":
        key = bytes(random.randint(0, 255) for _ in range(size))
    elif method == "lcg":                         
        key = bytearray()
        seed = 12345
        a, c, m = 1664525, 1013904223, 2**32
        x = seed
        for _ in range(size):
            x = (a * x + c) % m
            key.append(x & 0xFF)
        key = bytes(key)
    else:
        key = secrets.token_bytes(size)

    with open(key_path, "wb") as f:
        f.write(key)
    print(f"Ключ сохранён: {key_path} ({len(key)} байт)\n")
    return key_path


def vernam_encrypt(plaintext_path: str, key_path: str, ciphertext_path: str):
    "Задача 2: Шифрование Вернама (XOR)"
    with open(plaintext_path, "rb") as f:
        plaintext = f.read()
    with open(key_path, "rb") as f:
        key = f.read()

    if len(key) < len(plaintext):
        print("Предупреждение: Ключ короче текста! Ключ будет повторён.")
        key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]

    ciphertext = bytes(p ^ k for p, k in zip(plaintext, key))

    with open(ciphertext_path, "wb") as f:
        f.write(ciphertext)

    print(f"Зашифровано (Vernam): {ciphertext_path} ({len(ciphertext)} байт)")
    return ciphertext_path


def vernam_decrypt(ciphertext_path: str, key_path: str, decrypted_path: str):
    "Расшифрование Вернама"
    return vernam_encrypt(ciphertext_path, key_path, decrypted_path)


# ====================== RC4 ======================
def rc4_key_schedule(key: bytes):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def rc4_crypt(data: bytes, key: bytes) -> bytes:
    S = rc4_key_schedule(key)
    i = j = 0
    result = bytearray()
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)
    return bytes(result)


def rc4_file_encrypt(plaintext_path: str, key: bytes, ciphertext_path: str):
    with open(plaintext_path, "rb") as f:
        data = f.read()
    encrypted = rc4_crypt(data, key)
    with open(ciphertext_path, "wb") as f:
        f.write(encrypted)
    print(f"Зашифровано (RC4): {ciphertext_path} ({len(encrypted)} байт)")
    return ciphertext_path


# ====================== demo ======================
if __name__ == "__main__":
    print("=== Практическое задание 3: Шифр Вернама и потоковые шифры ===\n")

    os.makedirs("crypto_files", exist_ok=True)

    # Исправленный открытый текст (UTF-8)
    text = "Это секретное сообщение для демонстрации шифра Вернама и RC4. " * 50
    plaintext = text.encode('utf-8')

    with open("crypto_files/plaintext.txt", "wb") as f:
        f.write(plaintext)

    # 2. Генерация ключа
    key_path = "crypto_files/vernam_key.bin"
    generate_random_key_file(key_path, len(plaintext), method="urandom")

    # 3. Шифр Вернама
    cipher_path = "crypto_files/vernam_cipher.bin"
    decrypted_path = "crypto_files/vernam_decrypted.txt"

    vernam_encrypt("crypto_files/plaintext.txt", key_path, cipher_path)
    vernam_decrypt(cipher_path, key_path, decrypted_path)

    # 4. RC4
    rc4_key = secrets.token_bytes(16)
    rc4_cipher_path = "crypto_files/rc4_cipher.bin"
    rc4_decrypted_path = "crypto_files/rc4_decrypted.txt"

    rc4_file_encrypt("crypto_files/plaintext.txt", rc4_key, rc4_cipher_path)
    
    # Расшифрование RC4
    with open(rc4_cipher_path, "rb") as f:
        enc_data = f.read()
    decrypted_rc4 = rc4_crypt(enc_data, rc4_key)
    with open(rc4_decrypted_path, "wb") as f:
        f.write(decrypted_rc4)

    print("\n" + "="*70)
    print("ДЕМОНСТРАЦИЯ УСПЕШНО ЗАВЕРШЕНА!")
    print("Все файлы находятся в папке: crypto_files/")
    print("="*70)
