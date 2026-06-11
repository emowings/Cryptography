def modular_exponentiation(base: int, exponent: int, modulus: int):
    """
    Односторонняя функция быстрого возведения в степень по модулю
    (Binary Exponentiation / Exponentiation by Squaring)
    """
    if modulus == 1:
        return 0
    
    # Инициализация
    result = 1
    base = base % modulus
    multiplications = 0
    steps = []
    
    print(f"{'='*80}")
    print(f"Вычисление: {base}^{exponent} mod {modulus}")
    print(f"{'='*80}")
    print(f"{'Шаг':<4} {'Экспонента':<12} {'База':<12} {'Результат':<12} {'Действие':<20} {'Умножений'}")
    print(f"{'-'*80}")
    
    step = 0
    original_exponent = exponent
    
    while exponent > 0:
        step += 1
        current_step = f"{step:2d}"
        
        # Запоминаем состояние перед операциями
        action = ""
        
        # Если текущий бит экспоненты = 1
        if exponent % 2 == 1:
            # result = (result * base) % modulus
            old_result = result
            result = (result * base) % modulus
            multiplications += 1
            action = f"result *= base  (бит=1)"
            steps.append((original_exponent - exponent, old_result, base, result))
        
        # Квадратичное возведение базы
        old_base = base
        base = (base * base) % modulus
        multiplications += 1
        action2 = "base = base²"
        
        if exponent % 2 == 1:
            print(f"{current_step:<4} {exponent:<12} {old_base:<12} {result:<12} {action:<20} {multiplications}")
        else:
            print(f"{current_step:<4} {exponent:<12} {old_base:<12} {result:<12} {action2:<20} {multiplications}")
        
        exponent //= 2
    
    print(f"{'-'*80}")
    print(f"ИТОГО: {base}^{original_exponent} ≡ {result} (mod {modulus})")
    print(f"Количество умножений: {multiplications}")
    print(f"{'='*80}\n")
    
    return result, multiplications


def test_hamming_weight():
    "Тестирование на числах с разным весом Хэмминга"
    print("ТЕСТИРОВАНИЕ НА ЧИСЛАХ С РАЗНЫМ ВЕСОМ ХЭММИНГА\n")
    
    tests = [
        (5, 10, 10007),      # 1010b — 2 единицы
        (5, 15, 10007),      # 1111b — 4 единицы
        (5, 16, 10007),      # 10000b — 1 единица
        (5, 255, 10007),     # 11111111b — 8 единиц
        (123, 123456789, 1000000007),
    ]
    
    for base, exp, mod in tests:
        print(f"Экспонента = {exp} (вес Хэмминга = {bin(exp).count('1')})")
        result, mults = modular_exponentiation(base, exp, mod)
        # Проверка встроенной функцией
        check = pow(base, exp, mod)
        print(f"Проверка pow(): {check} → {' Совпадает' if result == check else '❌ Ошибка'}")
        print(f"Умножений выполнено: {mults}\n")


if __name__ == "__main__":
    print("=== Практическое задание: Быстрое возведение в степень ===\n")
    test_hamming_weight()
