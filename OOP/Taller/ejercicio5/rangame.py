from random import randint

def main():
    number = randint(1, 15)
    while True:
        try:
            num_user = int(input("Ingrese un numero entero del 1 al 15: "))
        except ValueError:
            print("Numero inválido")
            continue
        if num_user > number:
            print("El número es mayor!")
        elif num_user < number:
            print("El número es menor!")
        else:
            print("Ganaste!")
            break


if __name__ == "__main__":
    main()