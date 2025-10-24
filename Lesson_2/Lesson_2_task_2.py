def is_year_leap(year):
    """
    Проверяет, является ли год високосным
    Возвращает True, если год делится на 4 без остатка
    """
    if year % 4 == 0:
        return True
    else:
        return False

# Основная часть программы
chosen_year = 2024  # Выбираем год для проверки
result = is_year_leap(chosen_year)

print(f"год {chosen_year}: {result}")
def is_year_leap(year):
    """
    Проверяет, является ли год високосным
    Возвращает True, если год делится на 4 без остатка
    """
    if year % 4 == 0:
        return True
    else:
        return False

# Основная часть программы
chosen_year = 2023  # Выбираем год для проверки
result = is_year_leap(chosen_year)

print(f"год {chosen_year}: {result}")


