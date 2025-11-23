import math
def square(side):
    """
    Вычисляет площадь квадрата
    Если сторона не целая, округляет результат вверх
    """
    area = side * side
    # Округляем вверх, если результат не целый
    if not area.is_integer():
        return math.ceil(area)
    return area

# Тестируем функцию
print("Тест 1: сторона 5")
print(f"Площадь: {square(5)}")  # 25

print("\nТест 2: сторона 3.5")
print(f"Площадь: {square(3.5)}")  # 12.25 → 13 (округление вверх)

print("\nТест 3: сторона 2.0")
print(f"Площадь: {square(2.0)}")  # 4 (целое, без округления)

