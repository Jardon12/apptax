respuesta_positiva = ["Sí", "Si", "sí", "si"]

print("Bienvenido a Rent4you!\n")
print("Vamos a proceder a calcular tu IRPF...\n")
name = input("Antes de nada, ¿Cómo te llamas? ")
def rendimientos_trabajo():
    print("Hola", name, ". Comencemos calculando tus rendimientos del trabajo.")
    discapacidad = input("¿Tienes reconocido algún grado de discapacidad? \n")
    if discapacidad in respuesta_positiva:
        while True:
            grado_discapacidad = input("En ese caso, ¿Qué grado de discapacidad tienes reconocido? (para un 33% ponga, por favor, 33) ")
            try:
                grado_discapacidad = float(grado_discapacidad)
                if grado_discapacidad > 100:
                    print("Número incorrecto. No se puede tener una discapacidad superior al 100%")
                else:
                    confirmacion = input("{}% es el grado de discapacidad que has introducido. ¿Es correcto? ".format(grado_discapacidad))
                    if confirmacion.upper in respuesta_positiva:
                        break
                    else:
                        print("Por favor, inténtelo de nuevo")
            except:
                print("Algo ha ocurrido. Inténtelo de nuevo")

    check_renta = input("¿Percibes un sueldo o salario?\n")
    if check_renta in respuesta_positiva:
        renta = float(input("Cual es tu renta anual? "))
        # hablar de los rendimientos en especie


        #Gastos deducibles
        seguridad_Social = float(input("¿Cuál es el importe anual de tus cotizaciones a la Seguridad Social? "))
        sindicatos = float(input("¿Cuál es el importe anual de las cuotas satisfechas a sindicatos? "))
        defensa_juridica = float(input("¿Cuál ha sido el importe de los gastos de defensa juridica derivados de pleitos con tu empresa? "))
        if defensa_juridica > 300.00:
            defensa_juridica == 300.00
        otros_gastos = 2000.00
        if discapacidad in respuesta_positiva:
            if grado_discapacidad >= 0.33 and grado_discapacidad < 0.66:
                otros_gastos == otros_gastos + 3500.00
            elif grado_discapacidad >=0.66:
                otros_gastos == otros_gastos + 7750.00

        gastos_deducibles = seguridad_Social + sindicatos + defensa_juridica
        rendimientos_netos_trabajo = float(renta - gastos_deducibles)

        #calculo rendimiento neto reducido del trabajo
        if rendimientos_netos_trabajo <= 13115:
            rntr = rendimientos_netos_trabajo - 5565
            if rntr < 0:
                rntr = 0

        elif rendimientos_netos_trabajo <=16825:
            rntr = rendimientos_netos_trabajo - (5565 - 1.5*(rendimientos_netos_trabajo-13115))
            if rntr < 0:
                rntr = 0
        else:
            rntr = rendimientos_netos_trabajo
        print("Tus rendimientos netos reducidos del trabajo son", rntr)


def rendimientos_capital_inmobiliario():
    #Cálculo de los rendimientos del capital inmobiliario

    print("Pasemos a calcular tus rendimientos del capital inmobiliario..\n")
    check_capital_inmobiliario = input("¿Tienes algún inmueble alquilado, cedido,...etc?\n ")
    if check_capital_inmobiliario in respuesta_positiva:
        alquiler = float(input("Por favor, introduce el importe de la renta anual (con independencia de si ha sido cobrada o no) \n"))
        reparacion = float(input("Por favor, introduzca el importe de las reparaciones realizadas durante el año en el inmueble: \n"))
        check_intereses = input("¿Ha pagado intereses por la hipoteca del inmueble durante este año? \n")
        if check_intereses in respuesta_positiva:
            intereses = float(input("Por favor, introduce el importe de los intereses pagados durante este ejercicio:\n"))
        ibi = float(input("Por favor, introduzca el importe del IBI pagado este año por este inmueble: \n"))
        gastos_comunidad = float(input("Por favor, introduzca el importe de los gastos de comunidad pagados durante este ejercicio por razón de este inmueble: \n"))
        check_deudas = input("¿El inquilino no ha pagado alguna de las mensualidades y han transcurrido más de 6 meses desde que ha reclamado el cobro?\n ")
        if check_deudas in respuesta_positiva:
            deudas = float(input("Por favor, introduzca el importe total de estas mensualidades no cobradas:\n "))
        else:
            deudas = 0
        valor_catastral = float(input("Por favor, introduzca el valor catastral del inmueble, excluido el suelo: \n"))
        coste_adquisicion = float(input("Por favor, introduzca el precio pagado por el inmueble cuando se adquirió, excluido el valor del suelo: \n"))
        if valor_catastral > coste_adquisicion:
            amortizacion = 0.03 * valor_catastral
        else:
            coste_adquisicion = 0.03 * coste_adquisicion
        gastos_limitados = intereses + reparacion
        if gastos_limitados > alquiler:
            gastos_limitados == alquiler
        gastos_deducibles_inmuebles = float(gastos_limitados + ibi + gastos_comunidad + deudas + amortizacion)
        rendimientos_netos_capital_inmobiliario = float(alquiler - gastos_deducibles_inmuebles)
        destino_vivienda_habitual = input("¿El inmueble alquilado está destinado a vivienda habitual?\n ")
        if destino_vivienda_habitual in respuesta_positiva:
            rncir = 0.4 * rendimientos_netos_capital_inmobiliario
        else:
            rncir = rendimientos_netos_capital_inmobiliario
        print("Tus rendimientos netos reducidos del capital inmobiliario son", rncir, "\n")

def rendimientos_capital_mobiliario():
    #Cálculo rendimientos del capital mobiliario

    print("Pasemos a calcular tus rendimientos del capital mobiliario...\n")
    check_capital_mobiliario = input("¿Percibes rendimientos del capital mobiliario? (dividendos, intereses,...etc) \n")
    if check_capital_mobiliario in respuesta_positiva:
        dividendos = float(input("Por favor introduzca el importe de los dividendos brutos percibidos durante el año: \n"))
        intereses = float(input("Por favor introduzca el importe de los intereses brutos percibidos durante el año: \n"))
        gastos_administracion_deposito = float(input("Por favor introduzca el importe de los gastos de administración y custodia de su cuenta de valores\n"))
        retenciones_capital_mobiliario = 0.19 * (dividendos + intereses)
        rendimientos_netos_capital_mobiliario = float(dividendos + intereses - gastos_administracion_deposito)
        print("Tus rendimientos netos reducidos del capital mobiliario son", rendimientos_netos_capital_mobiliario, "\n")

def ganancias_patrimoniales():
    #Cálculo ganancias patrimoniales
    check_ganancias_patrimoniales = input("¿Ha tenido alguna ganancia o pérdida patrimonial durante el ejercicio? \n")
    if check_ganancias_patrimoniales in respuesta_positiva:
        numero_operaciones = int(input("¿Cuántas operaciones de venta ha realizado durante el año? \n"))
        valor_adquisicion_lista = []
        valor_transmision_lista = []
        for i in range(0, numero_operaciones):
            valor_adquisicion = float(input("Introduzca el valor de adquisicion (en negativo)\n"))
            valor_adquisicion_lista.append(valor_adquisicion)
            valor_transmision = float(input("Introduzca el valor de venta\n"))
            valor_transmision_lista.append(valor_transmision)
        ganancia_patrimonial = [valor_transmision_lista + valor_adquisicion_lista]
        for i in ganancia_patrimonial:
            print("Tus ganancias/pérdidas patrimoniales son", sum(i))

def main():
    menu ='''
    1. Rendimientos del trabajo.
    2. Rendimientos del capital inmobiliario
    3. Rendimientos del capital mobiliario
    4. Ganancias o pérdidas patrimoniales
    '''

    while True:
        print(menu)
        decision = input("¿Qué quieres introducir?\n ")
        if decision == "1":
            rendimientos_trabajo()
        elif decision == "2":
            rendimientos_capital_inmobiliario()
        elif decision == "3":
            rendimientos_capital_mobiliario()
        elif decision == "4":
            ganancias_patrimoniales()
        else:
            print('Something happened. Please try again.')

if __name__ == '__main__':
    main()