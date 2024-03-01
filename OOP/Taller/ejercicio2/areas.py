from math import pi

def main():
    
    while True:
        shape = input("Defina la figura para concer su área, puede ser circulo(C), rectangulo(R) o cubo(Q): ").lower()
        match (shape):
            case "circulo" | "c":
                try:
                    radio = float(input("Indique el radio de la circunferencia: "))
                    print(f"Perimetro: {2 * pi * radio}, área: {pi * radio**2}")
                    break
                except ValueError:
                    print("Valor inválido")
                    continue
            case "rectangulo" | "r":
                try:
                    base, altura = map(float, input("Indique base y altura separando por comas: ").split(","))
                    print(f"Área: {base * altura}")
                    break
                except ValueError:
                    print("Valor inválido")
                    continue
            case "cubo" | "q":
                try:
                    arista = float(input("Indique la longitud de la arista: "))
                    print(f"Volumen: {arista**3}")
                    break
                except ValueError:
                    print("Valor inválido")
                    continue
            case _:
                print("Figura inválida")


if __name__ == "__main__":
    main()