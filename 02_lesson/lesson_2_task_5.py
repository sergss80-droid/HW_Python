def month_of_season (month):
    if 3 <= month <= 5:
        return "Spring"
    if 6 <= month <= 8:
        return "Summer"
    if 9 <= month <= 11:
        return "Autumn"
    if  month in (1, 2, 12):
        return "Winter"
    return "неверный номер месяца"
month = int(input("Введите номер месяца (1-12): "))
print(month_of_season (month))
