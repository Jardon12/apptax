print("Bienvenido a Rent4you!\n")
print("Vamos a proceder a calcular tu IRPF...\n")
name = input("Antes de nada, ¿Cómo te llamas? ")
print("Hola", name, ". Comencemos calculando tus rendimientos del trabajo.")

discapacidad = input("¿Tienes reconocido algún grado de discapacidad? ")
if discapacidad == "Sí" or discapacidad == "Si" or discapacidad == "sí" or discapacidad == "si":
    while True:
        grado_discapacidad = input("En ese caso, ¿Qué grado de discapacidad tienes reconocido? (para un 33% ponga, por favor, 33) ")
        try:
            grado_discapacidad = float(grado_discapacidad)
            if grado_discapacidad > 100:
                print("Número incorrecto. No se puede tener una discapacidad superior al 100%")
            else:
                confirmacion = input("{}% es el grado de discapacidad que has introducido. ¿Es correcto? ".format(grado_discapacidad))
                if confirmacion.upper == "Sí" or confirmacion.upper == "Si" or confirmacion.upper == "sí" or confirmacion.upper == "si":
                    break
                else:
                    print("Por favor, inténtelo de nuevo")
        except:
            print("Algo ha ocurrido. Inténtelo de nuevo")

def rnt(renta, gastos_deducibles): #calcula los rendimientos netos del trabajo
    """

    :param renta:
    :param gastos_deducibles:
    :return: renta - gastos deducibles
    """
    rendimientos_netos_trabajo = float(renta - gastos_deducibles)
    if rendimientos_netos_trabajo < 0:
        rendimientos_netos_trabajo == 0
        print(rendimientos_netos_trabajo)
    else:
        print(rendimientos_netos_trabajo)


renta = float(input("Cual es tu renta anual? "))
# hablar de los rendimientos en especie


#Gastos deducibles
seguridad_Social = float(input("¿Cuál es el importe anual de tus cotizaciones a la Seguridad Social? "))
sindicatos = float(input("¿Cuál es el importe anual de las cuotas satisfechas a sindicatos? "))
defensa_juridica = float(input("¿Cuál ha sido el importe de los gastos de defensa juridica derivados de pleitos con tu empresa? "))
if defensa_juridica > 300.00:
    defensa_juridica == 300.00
otros_gastos = 2000.00
if discapacidad == "Sí" or discapacidad == "Si" or discapacidad == "sí" or discapacidad == "si":
    if grado_discapacidad >= 0.33 and grado_discapacidad < 0.66:
        otros_gastos == otros_gastos + 3500.00
    elif grado_discapacidad >=0.66:
        otros_gastos == otros_gastos + 7750.00

gastos_deducibles = seguridad_Social + sindicatos + defensa_juridica

print(f"Tus rendimientos netos del trabajo son {rnt(renta, gastos_deducibles)}")




