import os
import math
import random
from collections import Counter


def calculate_frequencies(file_path):
    "Задача 1: Подсчёт частот символов (байтов) в файле."
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        freq = Counter(data)
        total = len(data)
        frequencies = {byte: count / total for byte, count in freq.items() if count > 0}
        return frequencies, total
    except FileNotFoundError:
        print(f"Файл {file_path} не найден!")
        return {}, 0


def calculate_entropy(frequencies):
    "Задача 2: Вычисление информационной энтропии."
    if not frequencies:
        return 0.0
    entropy = 0.0
    for prob in frequencies.values():
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return entropy


def print_results(file_path, frequencies, entropy, size):
    """Вывод результатов."""
    print(f"\n{'='*60}")
    print(f"Файл: {file_path}")
    print(f"Размер: {size} байт")
    print(f"Энтропия: {entropy:.6f} бит/символ")
    print(f"Максимально возможная энтропия: {math.log2(256):.6f} бит/символ")
    print(f"Эффективность сжатия: {entropy / math.log2(256) * 100:.2f}%")
    print(f"Уникальных байтов: {len(frequencies)}")
    print("="*60)


def generate_test_files():
    """Задача 3: Генерация тестовых файлов."""
    os.makedirs("test_files", exist_ok=True)

    files = []

    # 1. Файл из одинаковых символов (энтропия ≈ 0)
    with open("test_files/constant.txt", "wb") as f:
        f.write(b'A' * 10000)
    files.append("test_files/constant.txt")

    # 2. Файл из случайных 0 и 1 (энтропия ≈ 1)
    with open("test_files/random_binary.bin", "wb") as f:
        data = bytes(random.randint(0, 1) for _ in range(10000))
        f.write(data)
    files.append("test_files/random_binary.bin")

    # 3. Файл со случайными байтами 0-255 (энтропия ≈ 8)
    with open("test_files/random_bytes.bin", "wb") as f:
        data = bytes(random.randint(0, 255) for _ in range(10000))
        f.write(data)
    files.append("test_files/random_bytes.bin")

    # 4. Текстовый файл (английский текст)
    text = """The quick brown fox jumps over the lazy dog. 
    Information entropy is a measure of uncertainty in a random variable.
    This is a sample text file for entropy calculation.""" * 200
    with open("test_files/text_sample.txt", "w", encoding="utf-8") as f:
        f.write(text)
    files.append("test_files/text_sample.txt")

    # 5. Файл с повторяющимися паттернами
    with open("test_files/repeating.bin", "wb") as f:
        pattern = b"ABC123" * 1667
        f.write(pattern)
    files.append("test_files/repeating.bin")

    return files


if __name__ == "__main__":
    print("=== Вычисление информационной энтропии файлов ===\n")

    # Генерируем тестовые файлы
    test_files = generate_test_files()

    print("Анализ сгенерированных файлов:\n")

    for file in test_files:
        freq, size = calculate_frequencies(file)
        entropy = calculate_entropy(freq)
        print_results(file, freq, entropy, size)
