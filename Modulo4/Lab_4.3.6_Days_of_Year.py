'''
Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, 
o devuelve None si cualquiera de los argumentos no es válido.

Debes utilizar las funciones previamente escritas y probadas. 
Agrega algunos casos de prueba al código.
'''

def is_year_leap(year):
    if year < 1582:
        return None
    else:
        return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def days_in_month(year, month):
    bisiesto = is_year_leap(year)
    if bisiesto == None or month not in range(1, 13): return None
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and bisiesto: months[1] += 1
    return months[month - 1]

def day_of_year(year, month, day):
    days = days_in_month(year, month)
    if days == None or day not in range(1, 32): return None
    if month > 1:
        for i in range(1, month):
            days += days_in_month(year, i)
    return days - (days_in_month(year, month) - day)
    

test_years = [1900, 2000, 1987, 2016]
test_months = [2, 2, 1, 9]
test_days = [10, 29, 25, 30]
test_results = [41, 60, 25, 274]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    dy = test_days[i]
    print(yr, mo, dy, "->", end="")
    result = day_of_year(yr, mo, dy)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
