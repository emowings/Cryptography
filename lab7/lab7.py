import math


def mod_pow(base: int, exp: int, mod: int) -> tuple:
    "Быстрое возведение в степень с подсчётом умножений"
    if mod == 1:
        return 0, 0
    result = 1
    base = base % mod
    multiplications = 0
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
            multiplications += 1
        base = (base * base) % mod
        multiplications += 1
        exp //= 2
    return result, multiplications


def discrete_log_brute_force(g: int, h: int, p: int):
    "Задача 2: Метод полного перебора"
    print(f"\n{'='*80}")
    print(f"МЕТОД ПОЛНОГО ПЕРЕБОРА: g^x ≡ h (mod p)")
    print(f"g = {g}, h = {h}, p = {p}")
    print(f"{'='*80}")
    
    multiplications = 0
    for x in range(p):
        y, mults = mod_pow(g, x, p)
        multiplications += mults
        if y == h:
            print(f"Решение найдено: x = {x}")
            print(f"Количество умножений: {multiplications}")
            return x, multiplications
    print("Решение не найдено")
    return None, multiplications


def baby_step_giant_step(g: int, h: int, p: int):
    "Задача 1: Метод Шэнкса (Baby-Step Giant-Step)"
    print(f"\n{'='*80}")
    print(f"МЕТОД ШЭНКСА (Baby-Step Giant-Step)")
    print(f"g = {g}, h = {h}, p = {p}")
    
    # Автоматический выбор m
    m = math.ceil(math.sqrt(p - 1))
    print(f"Автоматически выбрано m = k ≈ √(p-1) = {m}\n")
    
    # ====================== BABY STEPS ======================
    print("1. Baby Steps (вычисление таблицы):")
    baby_table = {}
    current = 1
    baby_mults = 0
    
    for j in range(m):
        baby_table[current] = j
        print(f"   g^{j:3d} ≡ {current:6d} (mod {p})")
        
        # Следующий baby step: current = current * g % p
        current, mult = mod_pow(current, 1, p)  # просто умножение на g
        baby_mults += mult
    
    print(f"   Таблица Baby Steps готова ({len(baby_table)} записей)")
    print(f"   Умножений в Baby Steps: {baby_mults}\n")
    
    # ====================== GIANT STEPS ======================
    print("2. Giant Steps:")
    giant_mults = 0
    factor, mult = mod_pow(g, m, p)           # g^m
    giant_mults += mult
    inv_factor, mult = mod_pow(factor, p-2, p)  # (g^m)^(-1) = g^{-m}
    giant_mults += mult
    
    current = h % p
    total_mults = baby_mults + giant_mults
    
    for i in range(m):
        print(f"   Шаг {i:2d}: h * g^(-{i}*m) ≡ {current:6d} (mod {p})", end="")
        
        if current in baby_table:
            j = baby_table[current]
            x = i * m + j
            total_mults += giant_mults  # добавляем умножения giant steps
            print(f"  ← СОВПАДЕНИЕ! x = {x}")
            print(f"\nРешение: x = {x}")
            print(f"Общее количество умножений: {total_mults}")
            return x, total_mults
        else:
            print()
        
        # current = current * g^{-m} % p
        current, mult = mod_pow(current, 1, p)  # умножение на inv_factor
        giant_mults += mult
        total_mults += mult
    
    print("Решение не найдено")
    return None, total_mults


def compare_methods():
    """Сравнение двух методов"""
    print("=== СРАВНЕНИЕ МЕТОДОВ ДИСКРЕТНОГО ЛОГАРИФМИРОВАНИЯ ===\n")
    
    # Маленький тест (для наглядности)
    tests = [
        (2, 6, 19),      # 2^x ≡ 6 mod 19 → x=14
        (5, 3, 23),      # 5^x ≡ 3 mod 23
        (10, 22, 47),
    ]
    
    for g, h, p in tests:
        print(f"\nТЕСТ: g={g}, h={h}, p={p}")
        
        # Brute Force
        print("\n--- Метод полного перебора ---")
        x1, mult1 = discrete_log_brute_force(g, h, p)
        
        # Baby-Step Giant-Step
        x2, mult2 = baby_step_giant_step(g, h, p)
        
        if x1 == x2:
            print(f"\n Оба метода дали одинаковый результат x = {x1}")
            print(f"Перебор:      {mult1} умножений")
            print(f"Шэнкс:        {mult2} умножений")
            print(f"Ускорение:    {mult1/mult2:.1f}x")
        print("-" * 80)


if __name__ == "__main__":
    compare_methods()
