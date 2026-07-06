def month_to_season(month):
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    if month in (1, 2, 12):
        return "Зима"
    return "неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))
