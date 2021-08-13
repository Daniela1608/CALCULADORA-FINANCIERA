
import financial_controller as financial


def lanzar():
  """
    Inicializa la aplicación y llama en orden los métodos, para dar el flujo de la aplicación.
  """  
  iniciar_calculadora()
  capital, interes, plazo_meses, valor_seguro, abono_capital = solicitar_entradas()
  
  valor_cuota = financial.obtener_valor_cuota(capital, interes, plazo_meses)
  resultado_simulacion = financial.simular_credito( capital, interes, plazo_meses, valor_cuota, valor_seguro, abono_capital )
  
  mostrar_resultados( capital, valor_cuota, valor_seguro, resultado_simulacion, abono_capital )
  fin_calculadora()
  financial.graficar_simulacion(resultado_simulacion, valor_seguro)
  firma()



def iniciar_calculadora():
  """
    Interfaz en consola de la calculadora financiera
  """
  print("""*****************************************************************************
***********************  CALCULADORA FINANCIERA  ****************************
*****************************************************************************
  """)
  

def fin_calculadora():
  """
    Interfaz en consola de la calculadora financiera
  """
  print("""
*****************************************************************************
*************************  CALCULO FINALIZADO  ******************************
*****************************************************************************""")


def mostrar_resultados(capital_inicial, valor_cuota, seguro, simulacion, abono_capital):
  print()
  print("Mes {}: Desembolso: {}".format(0, capital_inicial) )
  print("Valor de la cuota: {}".format(valor_cuota) )

  header = '|     Mes     |     Capital Base     |     Intereses     |     Seguro     |     Total Cuota     |     Abono a capital     |     Saldo después del pago     |'
  print( header )

  count = 0
  for data in simulacion:
    count += 1
    linea = '|'
    
    columan = ' {} '.format( data['mes'] )
    while len(columan) < 13:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['saldo_inicial'] )
    while len(columan) < 22:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['intereses'] )
    while len(columan) < 19:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( seguro )
    while len(columan) < 16:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['total_cuota'] )
    while len(columan) < 21:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['abono_capital'] )
    while len(columan) < 25:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['saldo_despues_pago'] )
    while len(columan) < 32:
      columan = ' ' + columan
    linea += columan + '|'

    print( linea )





def firma():
  """
    Muestra el nombre del creador de la aplicacion
  """
  firma = {
    'nombre': 'Laura Gonzalez Colorado', # Colocar su nombre completo
  }
  print("Este desarrollo fue creado por: {}".format(firma['nombre']))
  return firma['nombre']
  


def solicitar_entradas() -> tuple:
  # TODO: Documentar este código
  # TODO: Desarrollar este código
  capital= float(input("Ingresa el monto solicitado: "))
  interes= float(input("Ingresa en intereses en efectivo anual: "))
  interes= interes/100
  plazo_meses= int(input("Ingresa la cantidad de meses: "))
  valor_seguro= float(input("Ingrese el valor del seguro: "))
  abono_capital= float(input("Ingrese el abono al capital: "))


  #crear las 5 variables.
  
  
  return capital, interes ,plazo_meses,  valor_seguro, abono_capital 
  
  