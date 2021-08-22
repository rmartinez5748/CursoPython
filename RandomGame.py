import random

n = random.randint(1, 99)
intentos = 0
while True:
    trial = int(input("Guesss?: "))
    if trial == n:
        intentos = intentos+1
        print(f"felcidades, has advinidad el numero en el intento {intentos}")
        break

    else:
        if trial > n:
            print("El numero a a divinar es mas bajo")
            intentos = intentos+1
        else:
            print("El numero a adivinar es mas alto")
            intentos = intentos+1
