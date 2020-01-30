class Calculadora:
    def __init__(self,numero1,numero2):
        self.numero1=numero1
        self.numero2=numero2
    
    def sumar(self):
        try:
            resultado= self.numero1 + self.numero2
            print("la suma de {} y {} es {}".format(self.numero1,self.numero2,resultado))
        except TypeError:
            print("tipo de dato debe ser numerico")
        except:
            print("error al sumar")



    def restar(self):
        try:
            resultado= self.numero1 - self.numero2
            print("la resta de {} y {} es {}".format(self.numero1,self.numero2,resultado))
        except TypeError:
            print("tipo de dato debe ser numerico")
        except:
            print("error al restar")

    

    def multiplicar(self):
        try:
            resultado= self.numero1 * self.numero2
            print("la multiplicacion de {} y {} es {}".format(self.numero1,self.numero2,resultado))
        except TypeError:
            print("tipo de dato debe ser numerico")
        except:
            print("error al multiplicar")


    def dividir(self):
        try:
            resultado= self.numero1 / self.numero2
            print("la division de {} y {} es {}".format(self.numero1,self.numero2,resultado))
        except ZeroDivisionError:
            print ("no se puede dividir entre cero")
        except TypeError:
            print("tipo de dato debe ser numerico")
        except:
            print("error al dividir")



    def potenciar(self):
        try:
            resultado= self.numero1 ** self.numero2
            print("la potenciacion de {} y {} es {}".format(self.numero1,self.numero2,resultado))
        except TypeError:
            print("tipo de dato debe ser numerico")
        except:
            print("error al potenciar")

  