from datetime import datetime

class Rental:

        
    def rent_book(self, checkout, current_day, library):
        self.current_day = current_day
        self.serial_number = checkout[3]
        self.status = checkout[2]
        self.discount = checkout[1]
        self.name = checkout[0]
        self.library = library
        print()

        for i in range(len(self.library)):
            if self.serial_number == self.library[i][5] and self.library[i][4] > 0:
                print(f"El precio por dia del libro {self.library[i][0]} es {self.library[i][3]}$")
                
                if self.status == "employee":
                    print("Como eres empleado tienes un 40%% de descuento")
                    price_day = round(self.library[i][3] * self.discount)
                    print(f"Tu nuevo precio diario es {price_day}$, el total por 7 dias es {price_day * 7}$")
                    print(f"El precio diario por dia de atraso es 3 veces mayor que el normal: {price_day * 3}$")
                    print()
                    self.rent_list = [self.name, self.serial_number, self.current_day, self.current_day + 7, price_day, price_day * 3, "si"]
                elif self.status == "customer":
                    print(f"El precio diario por dia de atraso es 3 veces mayor que el normal: {self.library[i][3] * 3}$")
                    price_day = round(self.library[i][3] * self.discount)
                    self.rent_list = [self.name, self.serial_number, self.current_day, self.current_day + 7, price_day, price_day * 3, "no"]

                self.library[i][4] -= 1
                print()
                print(f"Hoy es el dia {self.current_day} por lo que tienes hasta el dia {self.current_day + 7} para devolver el libro sin atrasos")
                return self.rent_list, self.library
      
        print("Numero de serie no encontrado")
        return 0, self.library
    

    def return_book(self, all_rent, name, status, library, max, day, personal_debt):
        x = 0
        t = True
        if max == 0:
            print("No tienes libros arrendados")
            return library
        
        while t == True:
            quantity = int(input("Cuantos libros vas a devolver?: "))
            if 0 <= quantity <= max:
                t = False
            else:
                print(f"Solo tienes {max} libros arrendados")
    
        for i in range(quantity):
            serial = int(input("Cual es el numero serial del libro que quieres devolver: "))
            for row in range(len(all_rent)):
                if serial == all_rent[row][1] and name == all_rent[row][0] and all_rent[row][6] == status:
                    for j in range(len(library)):
                        if library[j][5] == serial:
                            library[j][4] += 1
                    if (day - all_rent[row][2]) <= 7: 
                        debt = all_rent[row][4] * day - all_rent[row][2]
                        personal_debt.append([debt, name, status])
                        print(f"Tu entrega estuvo al dia, ahora debes: {debt}$")
                    elif (day - all_rent[row][2]) > 7:
                        debt = all_rent[row][4] * 7 + all_rent[row][5] * (day - all_rent[row][3])
                        personal_debt.append([debt, name, status])
                        print(f"Te atrasaste devolviendo el libro, ahora debes: {debt}$")

                    all_rent.pop(row)
                    x += 1

            if x == 0:
                print("No tienes arrendado un libro con ese numero serial.")

        return library, personal_debt


                

        
