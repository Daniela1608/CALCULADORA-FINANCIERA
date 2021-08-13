import matplotlib.pyplot as plt
import pandas as pd

#datos=[]

def simular_credito( capital, interes, plazo_meses, valor_cuota, valor_seguro, abono_capital ) -> dict:
  # TODO: Documentar Método
  # TODO: Desarrollar este método
 
  
  datos=[] 
  valor_cuota = obtener_valor_cuota(capital, interes, plazo_meses)
  total_cuota= valor_cuota + valor_seguro
  interes_mensual = convertir_interes_efectivo_anula_a_mensual(interes)
  #print(interes)

  monto=capital
  #print(plazo_meses)
  for i in range(0,plazo_meses):
    #print(i)
    intereses= round(monto*interes_mensual,2)
    saldo_despues_pago= round(calcular_nuevo_valor_adeudado(monto, interes ) + valor_seguro-total_cuota-abono_capital,2)

    if saldo_despues_pago >=0:
      
      mes1={
        'mes': i+1 ,
        'saldo_inicial': monto,
        'intereses': intereses,
      
        'abono_capital': abono_capital,
        'total_cuota':total_cuota,
        'saldo_despues_pago': saldo_despues_pago
      }
      datos.append(mes1)
    else:
      abono= round(abono_capital + saldo_despues_pago,2)
      saldo_despues_pago = round(calcular_nuevo_valor_adeudado(monto, interes) + valor_seguro-total_cuota-abono)
      if abono_capital != 0:
        abono_capital= round((monto + valor_seguro + intereses)- total_cuota,2)
        if abono_capital <0:
         abono_capital=0
      if total_cuota > (monto+ intereses + valor_seguro):
        total_cuota= monto+ intereses + valor_seguro
      #print(total_cuota, monto, valor_seguro, intereses) 

      mes1={
        'mes':i+1,
        'saldo_inicial': monto,
        'intereses': intereses,
        
        'abono_capital': abono_capital,
        'total_cuota':total_cuota,
        'saldo_despues_pago': saldo_despues_pago
      }
      datos.append(mes1)
      break
    monto= saldo_despues_pago
  return datos




def calcular_nuevo_valor_adeudado( capital, interes ) -> float:
  # TODO: Documentar Método
  # TODO: Desarrollar este método
  # AYUDA: usar el método "convertir_interes_efectivo_anula_a_mensual" para convertir el interes de anual a mensual
  #capital + capital * interes efectivo mensual = capital*(1 + interes efectivo mensual) factor comun de la expresion
  new_capital= capital* (1 + convertir_interes_efectivo_anula_a_mensual(interes))
  return round(new_capital,2)#capital + 1




def convertir_interes_efectivo_anula_a_mensual(interes):
  """
    Convierte el interes de efectivo anula a efectivo mensual
  """
  return ((1+ interes)**(1/12)-1)



def obtener_valor_cuota(monto, tasa, cuotas):
    """
    Retorna el valor actual de la cuota, para cuotas son fijas.
                
    Formula = R = P [(i (1 + i)**n) / ((1 + i)**n – 1)]. 
    Donde: 
        R = renta (cuota)
        P = principal (préstamo adquirido)
        i = tasa de interés
    """
    efectiva_mensual = convertir_interes_efectivo_anula_a_mensual(tasa)
    valor_cuota = monto * ( (efectiva_mensual * ((1 + efectiva_mensual)**cuotas)) / (((1 + efectiva_mensual)**cuotas) - 1) )
    valor_cuota = valor_cuota + 1 # método para evitar un més adicional (truco)

    #print(valor_cuota)
    return round( valor_cuota, 2)

def graficar_simulacion(datos, valor_seguro):
  #print(datos)
    df=pd.DataFrame(datos)
    df['Abono a Capital'] = df['total_cuota'] - df['intereses'] - valor_seguro
    df['Abono de Intereses'] =df['intereses']
    data = df.loc[:,['Abono a Capital','Abono de Intereses','mes']] 

    data.plot(x='mes',xlabel='NUMERO DE CUOTAS',ylabel='CUOTA TOTAL FIJA',title='SIMULACIÓN CALCULADORA FINANCIERA',kind="bar",stacked=True,figsize=(10,8))
    plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
    plt.show()

  
  
