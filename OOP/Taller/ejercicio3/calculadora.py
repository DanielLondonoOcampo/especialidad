def main():
    while True:
        try:
            numbers = to_float(input("Ingrese dos números separados por coma para realizar la operación: ").split(","))
        except (ValueError, TypeError):
            print("Número inválido")
            continue
        operacion = input("Ingrese la operación deseada, suma(S), resta(R), multiplicación(M), división(D): ").lower()
        match operacion:
            case "suma", "s":
                print(f"Resultado de la suma: {numbers[0] + numbers[1]}")
                break
            case "resta", "r":
                print(f"Resultado de la suma: {numbers[0] - numbers[1]}")
                break
            case "multiplicacion", "s":
                print(f"Resultado de la multiplicación: {numbers[0] * numbers[1]}")
                break
            case "division", "s":
                print(f"Resultado de la división: {numbers[0] / numbers[1]}")
                break
            case _:
                print("Operación no soportada")
                continue


def to_float(*args):
    return [float(arg) for arg in args]



if __name__ == "__main__":
    main()