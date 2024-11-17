def hello_func(greeting, name='you'):
    return '{},{}'.format(greeting, name)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['math','art']
info = {"name":'john', "age":22}

student_info(*courses, **info)

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #als eerste waarde 0 toevoegen om in de def dom de month -1 te vermijden

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month - 1] #-1 omdat we geen 0 hebben toegevoegd voor de waarde bij 0

print(days_in_month(2017, 7))