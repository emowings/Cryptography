import hashlib
import os
import json
import secrets
import string
from datetime import datetime


# ====================== 1. ХЕШ-ФУНКЦИЯ ======================
def hash_password(password: str, salt: bytes = None) -> tuple:
    "Хеширование пароля (SHA-256)"
    if salt is None:
        salt = secrets.token_bytes(16)  # 128-битная соль
    
    data = salt + password.encode('utf-8')
    hash_obj = hashlib.sha256(data)
    password_hash = hash_obj.hexdigest()
    
    return password_hash, salt


def verify_password(password: str, stored_hash: str, salt: bytes) -> bool:
    "Проверка пароля"
    computed_hash, _ = hash_password(password, salt)
    return computed_hash == stored_hash


# ====================== 2. СИСТЕМА АВТОРИЗАЦИИ ======================
USERS_FILE = "users.json"


def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def register_user(username: str, password: str):
    users = load_users()
    
    if username in users:
        print("Пользователь уже существует!")
        return False
    
    password_hash, salt = hash_password(password)
    
    users[username] = {
        "hash": password_hash,
        "salt": salt.hex(),          # сохраняем соль в hex
        "registered": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    save_users(users)
    print(f"Пользователь '{username}' успешно зарегистрирован!")
    return True


def login_user(username: str, password: str):
    users = load_users()
    
    if username not in users:
        print("Пользователь не найден!")
        return False
    
    user_data = users[username]
    stored_hash = user_data["hash"]
    salt = bytes.fromhex(user_data["salt"])
    
    if verify_password(password, stored_hash, salt):
        print(f"Успешный вход! Добро пожаловать, {username}!")
        return True
    else:
        print("Неверный пароль!")
        return False


def generate_strong_password(length=12):
    "Генерация сильного пароля"
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


# ====================== demo ======================
if __name__ == "__main__":
    print("=== Практическое задание: Хеш-функции и система авторизации ===\n")
    
    # Демонстрация хеширования
    print("1. Демонстрация хеширования:")
    pw = "MySecretPass123!"
    h, s = hash_password(pw)
    print(f"Пароль: {pw}")
    print(f"Хеш:    {h}")
    print(f"Соль:   {s.hex()}\n")
    
    # Регистрация пользователей
    print("2. Регистрация пользователей:")
    register_user("admin", "SuperStrongPass2025!")
    register_user("user1", generate_strong_password(14))
    register_user("student", "password123")   # слабый пароль для демонстрации
    
    # Попытки входа
    print("\n3. Проверка входа:")
    login_user("admin", "SuperStrongPass2025!")
    login_user("admin", "WrongPassword!")
    login_user("student", "password123")
    
    # Просмотр базы (только хеши!)
    print("\n4. Содержимое базы пользователей (хеши + salt):")
    users = load_users()
    for username, data in users.items():
        print(f"• {username:10} | Зарегистрирован: {data['registered']}")
    
    print("\n" + "="*60)
    print("Задание выполнено!")
    print("Хеш-функция: SHA-256 + salt")
    print("Реализована безопасная система авторизации")
    print(f"Данные сохранены в файл: {USERS_FILE}")
