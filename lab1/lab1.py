import string

def caesar_encrypt(plaintext, key):
    "Зашифрование шифром Цезаря."
    alphabet = string.ascii_lowercase
    shifted = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted)
    return plaintext.lower().translate(table)

def caesar_decrypt(ciphertext, key):
    "Расшифрование шифром Цезаря."
    alphabet = string.ascii_lowercase
    shifted = alphabet[-key:] + alphabet[:-key] if key != 0 else alphabet
    table = str.maketrans(alphabet, shifted)
    return ciphertext.lower().translate(table)

def find_key_known_plaintext(plaintext, ciphertext):
    "Задача 2: Атака по известному открытому тексту (known-plaintext attack)."
    plaintext = plaintext.lower()
    ciphertext = ciphertext.lower()
    for key in range(26):
        if caesar_encrypt(plaintext, key) == ciphertext:
            return key
    return None

def brute_force_decrypt(ciphertext):
    "Задача 3: Атака по шифрованному тексту (ciphertext-only) — все варианты."
    results = []
    for key in range(26):
        decrypted = caesar_decrypt(ciphertext, key)
        results.append((key, decrypted))
    return results

# Словарь для задачи 4
ENGLISH_WORDS = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
    "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
    "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
    "back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
    "even", "new", "want", "because", "any", "these", "give", "day", "most", "us",
    "hello", "world", "example", "text", "attack", "cipher", "caesar"
}

def score_text(text):
    "Оценка осмысленности текста (слова + частотность букв)."
    text_lower = text.lower()
    words = text_lower.split()
    word_score = sum(1 for word in words if word.strip(".,!?") in ENGLISH_WORDS)
    
    # Частотность английских букв
    freq_score = sum(1 for char in text_lower if char in 'etaoinshrdlucmfwypvbg')
    return word_score * 10 + freq_score

def auto_decrypt(ciphertext):
    "Задача 4: Автоматический поиск ключа с помощью словаря."
    best_key = 0
    best_score = -1
    best_text = ""
    for key in range(26):
        decrypted = caesar_decrypt(ciphertext, key)
        score = score_text(decrypted)
        if score > best_score:
            best_score = score
            best_key = key
            best_text = decrypted
    return best_key, best_text, best_score


# ==================== ДЕМО ====================
if __name__ == "__main__":
    print("=== Шифр Цезаря — Практическое задание ===\n")
    
    plaintext = "hello world example"
    key = 5
    encrypted = caesar_encrypt(plaintext, key)
    
    print(f"Открытый текст: {plaintext}")
    print(f"Ключ: {key}")
    print(f"Зашифрованный текст: {encrypted}\n")
    
    # Задача 1
    print("Задача 1 — Расшифрование:", caesar_decrypt(encrypted, key))
    
    # Задача 2
    found_key = find_key_known_plaintext(plaintext, encrypted)
    print(f"\nЗадача 2 — Known-plaintext attack: найден ключ = {found_key}")
    
    # Задача 3
    print("\nЗадача 3 — Ciphertext-only (все варианты):")
    for k, dec in brute_force_decrypt(encrypted):
        print(f"  Key {k:2d}: {dec}")
    
    # Задача 4
    best_k, best_t, score = auto_decrypt(encrypted)
    print(f"\nЗадача 4 — Автоматический подбор ключа:")
    print(f"  Лучший ключ: {best_k}")
    print(f"  Расшифровка: {best_t}")
    print(f"  Оценка: {score}")
