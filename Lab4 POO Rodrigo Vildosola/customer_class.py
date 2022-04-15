from person_class import Person


class Customer(Person):

    def __init__(self, x):
        self.order = ["Nombre", "Numero serial", "Dia de arriendo", "Fecha de entrega", "Precio diario", "Precio de atraso", "Empleado"]
        self.name = input("Escribe tu nombre: ")
        self.x = x
        if self.x == 0:
            self.serial = int(input("Que numero serial quieres: "))
        self.discount = 1

    def checkout(self):
        if self.x == 0:
            return [self.name, self.discount, "customer", self.serial]
        elif self.x == 1:
            return [self.name, self.discount, "customer"]


    def show_rented_total(self, rented_list):
        print()
        print("{: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >10}".format(*self.order))
        for row in rented_list:
            print("{: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >10}".format(*row))
        print()


    def show_rented_name(self, rented_list, name):
        x = 0
        print("{: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >10}".format(*self.order))
        for row in rented_list:
            if row[0] == name and row[6] == "no":
                x += 1
                print("{: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >10}".format(*row))
        if x == 0:
            print("No tienes libros arrendados.")
        
        return x