def main():
    while True:
        try:
            a, b = to_float(input("Ingrese dos números separados por coma para realizar la operación: ").split(","))
        except (ValueError, TypeError):
            print("Número inválido")
            continue
        operacion = input("Ingrese la operación deseada, suma(S), resta(R), multiplicación(M), división(D): ").lower()
        match operacion:
            case "suma", "s":
                print(f"Resultado de la suma: {a + b}")
                break
            case "resta", "r":
                print(f"Resultado de la suma: {a - b}")
                break
            case "multiplicacion", "s":
                print(f"Resultado de la multiplicación: {a * b}")
                break
            case "division", "s":
                print(f"Resultado de la división: {a / b}")
                break
            case _:
                print("Operación no soportada")
                continue


def to_float(*args):
    return [float(arg) for arg in args]



if __name__ == "__main__":
    main()