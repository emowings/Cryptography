import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import secrets


def generate_key(key_size: int = 32):
    "Генерация случайного ключа (по умолчанию AES-256)"
    key = secrets.token_bytes(key_size)
    print(f"Сгенерирован ключ длиной {len(key)*8} бит")
    return key


def save_key(key, filepath="aes_key.bin"):
    with open(filepath, "wb") as f:
        f.write(key)
    print(f"Ключ сохранён в {filepath}")


def load_key(filepath="aes_key.bin"):
    with open(filepath, "rb") as f:
        return f.read()


def encrypt_file(input_path: str, output_path: str, key: bytes):
    "Зашифрование файла с помощью AES-256 в режиме CBC"
    # Читаем данные
    with open(input_path, "rb") as f:
        plaintext = f.read()

    # Добавляем padding (PKCS7)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Генерируем случайный IV
    iv = secrets.token_bytes(16)

    # Шифрование
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Сохраняем IV + зашифрованные данные
    with open(output_path, "wb") as f:
        f.write(iv + ciphertext)

    print(f"Файл успешно ЗАШИФРОВАН: {output_path}")
    print(f"Размер: {len(plaintext)} → {len(iv + ciphertext)} байт")


def decrypt_file(input_path: str, output_path: str, key: bytes):
    """Расшифрование файла AES-256 CBC"""
    with open(input_path, "rb") as f:
        data = f.read()

    iv = data[:16]
    ciphertext = data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Убираем padding
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    with open(output_path, "wb") as f:
        f.write(plaintext)

    print(f"Файл успешно РАСШИФРОВАН: {output_path}")


# ====================== demo ======================
if __name__ == "__main__":
    print("=== Практическое задание 4: Блочные шифры (AES-256) ===\n")

    os.makedirs("block_cipher_files", exist_ok=True)

    # Создаём тестовый файл
    test_text = "Это тестовое сообщение для демонстрации блочного шифра AES-256.\n" * 100
    plaintext_path = "block_cipher_files/original.txt"
    with open(plaintext_path, "wb") as f:
        f.write(test_text.encode('utf-8'))

    # Генерация ключа
    key = generate_key(32)  # AES-256
    key_path = "block_cipher_files/aes_key.bin"
    save_key(key, key_path)

    # Пути к файлам
    encrypted_path = "block_cipher_files/encrypted.bin"
    decrypted_path = "block_cipher_files/decrypted.txt"

    # Шифрование
    encrypt_file(plaintext_path, encrypted_path, key)

    # Расшифрование
    decrypt_file(encrypted_path, decrypted_path, key)

    # Проверка
    print("\n" + "="*60)
    print("Проверка целостности:")
    with open(plaintext_path, "rb") as f:
        original = f.read()
    with open(decrypted_path, "rb") as f:
        decrypted = f.read()

    print("Расшифрование прошло успешно:", original == decrypted)
    print("="*60)
    print("\nФайлы созданы в папке: block_cipher_files/")
