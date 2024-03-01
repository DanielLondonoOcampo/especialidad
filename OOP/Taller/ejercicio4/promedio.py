import random

APROBADO = 3.5

def main():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de notas para calcular el promedio: "))
        except ValueError:
            print("Cantidad incorrecta")
            continue
        sum = 0
        for i in range(cantidad):
            try:
                nota = input(f"Indique el valor de la nota #{i + 1} o deje en blanco para un valor aleatorio: ")
                if nota != "":
                    sum+=float(nota)
                else:
                    sum+=random.uniform(0.0, 5.0)
            except ValueError:
                print("Valor inválido")
                break
        promedio = sum/cantidad
        if promedio >= APROBADO:
            print(f"Aprobado! Promedio de: {promedio}")
            break
        print(f"Reprobado :c Promedio de: {promedio}")
        break






if __name__ == "__main__":
    main()