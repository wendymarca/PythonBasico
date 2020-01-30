from motor import Motor
from vehiculo import Vehiculo
from simulador import Simulador
from calculadora import Calculadora

calcu=Calculadora("5",3)

 
#m1=Motor("85556",1000)
#m2=Motor("59981",2000)

#v1=Vehiculo("8074WTV","negro","nissan","2009","gasolina",2000,1500,True)
#v2=Vehiculo("2901DID","verde","toyota","2015","gas",1000,1000,True)
#v3=Vehiculo("100CTA","azul","chevrolet","2018","diesel",2500,2000,True)

#v1.poner_motor(m1)
#v2.poner_motor(m1)
#v3.poner_motor(m2)

#lista=[v1,v2,v3]
#s= Simulador(lista)
#s.iniciar_simulacion(2)

calcu.sumar()
calcu.restar()
calcu.multiplicar()
calcu.dividir()
calcu.potenciar()
