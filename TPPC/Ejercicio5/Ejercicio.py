class Operations:

    paid = 0.00
    left = 0.00
    factures = {}
    choice = ''

    def remove(self):
        print("Introduce el numero de la factura a pagar")
        key = input()
        self.paid += self.factures[key]
        self.left = self.left - self.factures[key]
        self.factures.pop(key)
        print("El total restante es de: " + str(float(self.left)))
        print("El total pagado hasta el momento es de: " + str(float(self.paid)))
        return self.left

    def add(self):
        print("Ingrese el numero de factura")
        fact = input()
        print("Ingrese el monto a pagar")
        suma = float(input())
        self.left = float(self.left) + float(suma)
        self.factures[fact] = suma
        print("El total a pagar es de :" + str((float(self.left))))
        print("El total pagado hasta el momento es de: " + str(float(self.paid)))
        return self.left


o = Operations()

while o.choice != '3':
    if o.choice == '1':
        o.add()
    o.choice = input("Bienvenido, por favor, seleccione la opción a realizar:" + "\n" + "1. Nueva Factura"
                     + "\n"
                     + "2. Pagar Factura" + "\n" + "3. Salir")
    if o.choice == '2':
        o.remove()
