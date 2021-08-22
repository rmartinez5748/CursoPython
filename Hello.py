weight = float(input("introduce your weight: "))

unit = input(("L(pounds) or K(kilograms): "))

if unit == "L":
    kg_weight = weight/2.2
    print(f'Your weight in kilograms is: {kg_weight}')

if unit == "K":
    p_weight = weight*2.2
    print(f'Your weight in pounds is: {p_weight}')
