def priem_getallen(max_getal: int = 1000)->dict:
    """
    Calculates de priem getallen
    Args:
        max_getal:

    Returns: dict

    """
    list_priem = {}
    for i in range(2, max_getal):
        for j in range(2, max_getal):
            if i % j==0 and i!=j:
                if list_priem.get(i) is None:
                    list_priem[i] = [j]
                else:
                    list_priem[i].append(j)
    return list_priem


if __name__ == "__main__":
    for key, value in  priem_getallen().items():
        print(f"{key} = {value}")

