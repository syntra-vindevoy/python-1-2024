


def oefening_1(t:list) -> tuple:

    list_n = len(t)
    list_sum = sum(t)
    list_min = sorted(t)[0]
    list_max = sorted(t)[-1]
    list_mean1 = list_sum / list_n
    list_mean2 = (list_min + list_max) / 2

    return list_n, list_sum, list_min, list_max, list_mean1, list_mean2

t = [2, 4, 6, 12, 8]
result = oefening_1(t)
print(result)


def oefening_2(name:str, first_name:str) -> str:
    return "".join(sorted(list(name.lower() + first_name.lower())))

print(oefening_2("Thomas", "Meersschaut"))


def oefening_3(names: list) -> dict:
    return {name: name.lower() + "@syntra.be" for name in names}

name = ["Thomas", "Jan", "Pieter"]
print(oefening_3(name))


def oefening_4():
    with open("namen.txt", "r") as f:
        names = f.read().splitlines()

        unique = []
        for name in names:
            if name.capitalize() not in unique:
                unique.append(name.capitalize())

    with open("uniek.txt", "w") as f:
        f.write("\n".join(unique))

oefening_4()


with open("landen.txt", "r") as f:
    countries = f.read().splitlines()

with open("verbruik.txt", "r") as f:
    usage = f.read().splitlines()
    usage = [item for item in usage if item]
    usage = [item for item in usage if ',2025,' not in item]


def total_usage(l_usage:list, cc:str) -> float:
    data = [tuple(item.split(',')) for item in l_usage]
    filtered_data = [item for item in data if item[0] == cc]
    total_sum = sum(float(item[3]) for item in filtered_data)
    return total_sum

def month_usage(l_usage:list, cc:str, min_usage:float) -> float:
    data = [tuple(item.split(',')) for item in l_usage]
    filtered_data1 = [item for item in data if item[0] == cc]

    fictional_usage = 0
    for month in range(1, 13):
        filtered_data = [item for item in filtered_data1 if item[2] == str(month)]
        for item in filtered_data:
            if float(item[3]) < min_usage:
                fictional_usage += min_usage
            else:
                fictional_usage += float(item[3])

    return fictional_usage


def oefening_5(countries:list, l_usage:list):
        d = {}

        for country in countries:
            parts = country.split(",")
            key = parts[0]
            usage = total_usage(l_usage, key)
            fict_usage = month_usage(l_usage, key, int(parts[2]))
            diff = max((fict_usage - usage), 0)
            total = usage + diff

            d[key] = (parts[1], total, diff)
            t = [(key, *value) for key, value in d.items()]

        t = sorted(t, key=lambda x: x[1])
        with open('2024.txt', 'w') as file:
            for item in t:
                file.write(','.join(map(str, item)) + '\n')

oefening_5(countries, usage)

