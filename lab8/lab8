from PIL import Image
import os


def text_to_bin(text: str) -> str:
    "Преобразование текста в битовую строку"
    return ''.join(format(ord(char), '08b') for char in text)


def bin_to_text(binary: str) -> str:
    "Преобразование битовой строки обратно в текст"
    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text


def embed_lsb(input_image_path: str, secret_message: str, output_image_path: str):
    "Внедрение сообщения методом LSB-replacement"
    img = Image.open(input_image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    pixels = list(img.getdata())
    binary_message = text_to_bin(secret_message + '\0')  # \0 — конец сообщения
    message_length = len(binary_message)
    
    if message_length > len(pixels) * 3:
        raise ValueError("Сообщение слишком большое для этого изображения!")
    
    print(f"Внедряем сообщение длиной {len(secret_message)} символов ({message_length} бит)")
    
    pixel_list = []
    bit_index = 0
    
    for i, pixel in enumerate(pixels):
        r, g, b = pixel
        
        if bit_index < message_length:
            # Заменяем младший бит красного
            r = (r & 0xFE) | int(binary_message[bit_index])
            bit_index += 1
        if bit_index < message_length:
            # Зеленый
            g = (g & 0xFE) | int(binary_message[bit_index])
            bit_index += 1
        if bit_index < message_length:
            # Синий
            b = (b & 0xFE) | int(binary_message[bit_index])
            bit_index += 1
        
        pixel_list.append((r, g, b))
    
    # Создаём новое изображение
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(pixel_list)
    new_img.save(output_image_path)
    
    print(f"Сообщение успешно внедрено!")
    print(f"Изображение сохранено как: {output_image_path}")
    print(f"Изменено {bit_index} бит\n")


def extract_lsb(image_path: str) -> str:
    """Извлечение сообщения методом LSB"""
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    pixels = list(img.getdata())
    binary_message = ''
    
    print("Извлечение сообщения...")
    
    for pixel in pixels:
        r, g, b = pixel
        binary_message += str(r & 1)
        binary_message += str(g & 1)
        binary_message += str(b & 1)
    
    # Ищем конец сообщения (нулевой байт)
    end_index = binary_message.find('00000000')
    if end_index != -1:
        binary_message = binary_message[:end_index]
    
    secret_text = bin_to_text(binary_message)
    print(f"Извлечённое сообщение: {secret_text}")
    return secret_text


# ====================== ДЕМО ======================
if __name__ == "__main__":
    print("=== LSB Steganography (Внедрение в BMP) ===\n")
    
    # Создаём тестовую папку
    os.makedirs("stego_images", exist_ok=True)
    
    input_image = "stego_images/cover.bmp"      # ← Замени на свой BMP
    output_image = "stego_images/stego_lsb.bmp"
    
    # Если нет изображения — создаём простое
    if not os.path.exists(input_image):
        print("Создаём тестовое изображение...")
        img = Image.new('RGB', (400, 300), color=(73, 109, 137))
        img.save(input_image)
    
    secret_message = "Это секретное сообщение для практического задания по стеганографии! " \
                     "LSB-replacement успешно работает. Python 2026."
    
    # Внедрение
    embed_lsb(input_image, secret_message, output_image)
    
    # Извлечение
    print("\n" + "="*50)
    extracted = extract_lsb(output_image)
    
    print("\n" + "="*60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА УСПЕШНО!")
    print("Метод: LSB-replacement")
    print(f"Оригинал: {input_image}")
    print(f"Стего:    {output_image}")
