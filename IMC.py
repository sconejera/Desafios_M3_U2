print("-------------------------------------------------------------------------")
print("Calcula el IMC a partir del peso y la altura")
print("Utilice (.) como separador decimal")
print("-------------------------------------------------------------------------")

def calcular_imc(peso, altura):

    imc = peso / ((altura/100) ** 2)
    return round(imc, 2)


def obtener_clasificacion_oms(imc):

    if imc < 18.5:
        return "Bajo Peso"
    elif imc < 25:
        return "Adecuado"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad Grado I"
    elif imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"


def main():

    # Solicita datos al usuario
    while True:
        try:
            peso = float(input("Ingrese su peso en kilogramos: "))
            if peso <=0:
                raise ValueError("El peso debe ser un valor positivo")
            break
        except ValueError:
            print("Error: El peso debe ser un número válido.")

    while True:
        try:
            altura = float(input("Ingrese su altura en centimetros: "))
            if altura <=0:
                raise ValueError("La altura debe ser un valor positivo")
            break
        except ValueError:
            print("Error: La altura debe ser un número válido.")

    # Calcula el IMC
    imc = calcular_imc(peso, altura)

    # Obtiene la clasificación OMS
    clasificacion_oms = obtener_clasificacion_oms(imc)

    # Muestra el resultados al usuario
    print(f"\nSu IMC es: {imc}")
    print(f"Su clasificación según la OMS es: {clasificacion_oms}")
    print("-------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
