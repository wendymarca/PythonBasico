class Vehiculo:
    FACTOR_EMISION_GASOLINA=2.196
    FACTOR_EMISION_DIESEL=2.471
    def __init__(self,placa,color,marca,modelo,combustible,km,tanque,AC):
        self.placa=placa
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.combustible=combustible
        self.km=km
        self.tanque=tanque
        self.AC=AC
        self.encendido=False
        self.litros_consumidos=0
     
    # def encender(self):
    #     self.encendido=True


    # def apagar(self):
    #     self.encendido=False

    def tocar_bocina(self):
        print("piii piii")

    def frenar(self):
        print("frenando")

    def obtener_combustible(self):
        return self.tanque
    

    def mostrar_vehiculo(self):
        print("la placa del vehiculo es" + self.placa)
        print("el color del vehiculo es" + self.color)
        print("la marca del vehiculo es"+  self.marca)
        print("el modelo del vehiculo es" + str(self.modelo))
        print("el tipo de combustible del vehiculo es" + self.combustible)
        print("el kilometraje del vehiculo es" + str(self.km))
        print("el tanque del vehiculo es" + str(self.tanque))
        print("el aire acondicionado del vehiculo es" + str(self.AC))      


    def cargar_combustible(self, litros):
        self.tanque+= litros
        print("cargando combustible")

    
    def recorrer_distancia(self, distancia):
        if self.motor.esta_encendido():
            variante= self.obtener_variante() 
            if distancia<(self.tanque*variante):
                self.km+=distancia
                total_litros=round(self.km/variante)
                self.tanque-=total_litros
                self.litros_consumidos+=total_litros
                print("recorriendo {} kilometros".format(distancia))
            else:
                print("no tienes suficiente combustible")
        else:
            print("el vehiculo esta apagado")
    

    def calcular_CO2(self):
        if self.combustible =="Gasolina":
            return self.FACTOR_EMISION_GASOLINA * self.litros_consumidos
        else:
            return self.FACTOR_EMISION_DIESEL * self.litros_consumidos


    
    def poner_motor(self,motor):
        self.motor=motor


    def obtener_variante(self):
        cilindrada=self.motor. obtener_cilindrada()
        if cilindrada==1000:
            return(12)
        elif cilindrada==2000:
            return(10)
        else:
            return(8)

    def hay_combustible(self,distancia):
        variante=self.obtener_variante()
        if not distancia<(variante*self.tanque):
            return False
        return True

    def obtener_informe(self):
        informe="\n-----------"
        informe+="\nINFORME FINAL-EMISION CO2"
        informe+="\n----------"
        informe+="\n Ud esta conduciendo un vehiculo marca {},modelo {},color {}".format(self.marca,self.modelo,self.color)
        informe+="\n Ha recorrido un total de {} KM de distancia".format(self.km)
        informe+="\n Ha consumido un total de {} litros de {}".format(self.litros_consumidos,self.combustible)
        informe+="\n En su tanque tiene {} litros de {} ".format(self.tanque,self.combustible)
        informe+="\n Se emitio a la atmosfera un total de {} kg de CO2".format(round(self.calcular_CO2(),2))
        return informe

    