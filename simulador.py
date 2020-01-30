import random 
class Simulador:
    def __init__(self,vehiculos):
        self.vehiculos=vehiculos
    
    def iniciar_simulacion(self,dias):
        for v in self.vehiculos:
            print("\n")
            print("VEHICULO{}".format(v))
            if not v.motor.esta_encendido():
                v.motor.encender()
            for dia in range(1,dias+1):
                print("--------------")
                print("Dia # {}".format(dia))
                print("--------------")
                distancia=random.randint(0,100)
                if not v.hay_combustible(distancia):
                    litros=random.randint(30,70)   
                    v.cargar_combustible(litros)
                v.recorrer_distancia(distancia)
            print(v.obtener_informe())
