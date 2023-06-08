class Calculadora():
        
    def suma(self, numero1, numero2):
        res = numero1 + numero2
        print("La suma entre",numero1, "y", numero2, "da igual a",res)
        
    def resta(self, numero1, numero2):
        res = numero1 - numero2
        print("La resta entre", numero1, "y", numero2, "da igual a",res)
        
    def multiplicacion(self, numero1, numero2):
        res = numero1 * numero2
        print ("La multiplicación entre",numero1, "y", numero2, "da igual a",res)
        
    def division (self, numero1, numero2):
        if numero2 != 0:
            res = numero1/numero2
            print ("La división entre",numero1, "y", numero2, "da igual a",res)
        else:
            print ("No se puede dividir por 0")
            
    def potencia (self, numero1, numero2):
        res = numero1 ** numero2
        print ("La potendia de",numero1, "elevado a la", numero2, "da igual a",res)
        