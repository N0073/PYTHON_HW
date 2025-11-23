def month_to_season(month):
    """
    Определяет сезон по номеру месяца
    Зима: 12, 1, 2
    Весна: 3, 4, 5
    Лето: 6, 7, 8
    Осень: 9, 10, 11
    """
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный месяц"
    # Тестируем функцию


test_months = [2, 5, 8, 12, 13]  # 13 — для проверки неверного значения

for month in test_months:
    season = month_to_season(month)
    print(f"Месяц {month}: {season}")