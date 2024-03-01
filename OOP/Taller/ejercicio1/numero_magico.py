MAGIC_NUMBER = 12345679

def main():
    user_number = int(input("Ingrese un número entero entre 1 y 9: "))

    while user_number < 1 or user_number > 9 :
        if isinstance(user_number, float):
            print("El numero debe ser un entero")
        user_number = int(input("Ingrese un número entero entre 1 y 9: "))

    print(f"El número mágico es: {calculate(user_number)}")


def calculate(num):
    num = num * 9 * MAGIC_NUMBER
    return num


if __name__ == "__main__":
    main()