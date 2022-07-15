from math import pi

class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise AttributeError("El valor del radio no debe ser menor o igual a 0")
        else:
            self._radio = radio

    class DescriptorRadio:
        def __set__(self, instance, valor): 
            if valor <= 0:
                    raise AttributeError("El nuevo valor del radio no debe ser menor o igual a 0")
            else:
                instance._radio = valor

    def __str__(self):
        return "Circulo de radio: {}".format(self._radio)
            
    def __mul__ (self, n): 
        if n <= 0:
            raise AttributeError("El multiplicador no debe ser menor o igual a 0")
        else:
            return Circulo (self._radio * n)

    def area_circulo (self,):
        self.area = pi * self._radio ** 2
        print("El area del circulo es: {:.2f}".format(self.area))

    def perimetro_circulo(self,):
        self.perimetro = pi ** 2 * self._radio
        print("El perimetro del circulo es: {:.2f}".format(self.perimetro))

    radio = DescriptorRadio()
        
if __name__ == "__main__":
    radio = int(input("Ingrese un radio:"))
    obj_circulo = Circulo(radio)
    print("------------------")
    print(obj_circulo)
    obj_circulo.area_circulo()
    obj_circulo.perimetro_circulo()

    print("------------------")
    x = obj_circulo *4
    print(x)
    x.area_circulo()
    x.perimetro_circulo()

    print("------------------")
    obj_circulo.radio = 6
    print(obj_circulo)
    obj_circulo.area_circulo()
    obj_circulo.perimetro_circulo()