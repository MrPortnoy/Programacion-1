#DATOS
none=0; dist0=18; dist1=25; dist2=32; dist3=40
normal=0; student=0.25; old=.5; invalid=1

def cargar_sube(numero):
  global saldo
  saldo+=numero

#invout=1.6; dist=dist2; user=normal; ultima_senial=3400000; saldo=25
print("AVISO: Siempre debes colocar el valor numerico de cada variable, los nombres son solo de guia\n")

print("Afirme si desea usar una tarjeta valida: invout=>1.6")
invout=float(input())

print("Elija su tarifa correspondiente: none=0; dist0=18; dist1=25; dist2=32; dist3=40")
dist=int(input())

print("Eliga el tipo de descuento: normal=0; student=0.25; old=.5; invalid=1")
user=float(input())

print("Afirme si realizo trasbordo dentro de la hora para obtener descuento: ultima_senial<=60 ")
ultima_senial=int(input())

print("¿Con cuanto saldo desea iniciar? Ej: saldo=25 o saldo=-25. Recuerda que el sistema te presta hasta -50")
saldo=int(input())

print("¿Quieres cargar saldo? Ej: numero=10 o numero=0 ")
numero=int(input())

cargar_sube(numero)

print("saldo actual" +" "+ str(saldo) + "\n\n")



#CODE
def hay_senial():
   return invout>=1.6

def tarifa():
  return dist

def desc_user():
  return user

def desc_time():
  if ultima_senial <= 60:
    return 0.1
  else:
    return 0

def desc_total():
  return tarifa()*(desc_time() + desc_user())

def precio_final():
  return (tarifa()-(desc_total()))

def saldo_inicial():
  return saldo

def restar():
  if (saldo_inicial() - precio_final())>=-50:
    return saldo_inicial() - precio_final()
  else:
    return saldo_inicial()

def saldo_final_provisorio():
  return restar()

saldo_final = float('{:.2f}'.format(saldo_final_provisorio()))

def cobrar_boleto():
  if (saldo_inicial() - precio_final())>=-50:
    print("Luz Verde")
    return restar()
  else:
    print("Saldo Insuficiente")
    print("Luz Roja")

def cobro_efectuado():
  return saldo_inicial()>saldo_final_provisorio()




#PROGRAM
print("Ejecutando Programa\n")
if tarifa()!=0:
  print("$"+str(tarifa()))
  if hay_senial():
    print("Espere...")
    cobrar_boleto()
    if cobro_efectuado():
      print("Saldo Anterior"+ " " + str(saldo) + " " +"|"+ " " + "Saldo Disponible" + " " +"$"+ str(saldo_final))
    else:
      print("Saldo Disponible" + " " +"$"+ str(saldo))
  else:
    print("Vuelve a Intentarlo")
    print("Luz Roja")
else:
  print("SUBE SUBE SUBE SUBE")