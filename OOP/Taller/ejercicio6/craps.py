from random import randint
from time import sleep

def main():
    while True:
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        suma = dado1 + dado2
        print("Lanzando los dados!")
        sleep(2)
        if suma == 7 or suma == 11:
            print("Ganaste!")
            break
        elif suma == 2 or suma == 3 or suma == 12:
            print("Perdiste!")
            break
        else:
            print("Nueva ronda!")
            sleep(1)



if __name__ == "__main__":
    main()