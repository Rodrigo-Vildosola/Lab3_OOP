from library_class import Library
from book_class import Book
from employee_class import Employee
from customer_class import Customer
from rental_class import Rental
from copybook_class import Copybook


t = True
all_debts = []
total_list = [[]]
all_rent = []
my_library = Library()
day = 1
print("---------------")
print("     Dia 1     ")
print("---------------")

while t == True:
    print()
    print("[1] Agregar un libro")
    print("[2] Ver inventario completo en la biblioteca")
    print("[3] Filtrar libros")
    print("[4] Arrendar un libro")
    print("[5] Devolver un libro")
    print("[6] Ver todos los arriendos")
    print("[7] Pagar deuda")
    print("[8] pasar dia")
    print("[9] Salir")
    x = input(": ")
    print()
    if x == "1":
        new_book = Book()
        book_info = new_book.book_information()
        serial = Copybook()
        
        total_list = serial.final_info(book_info, total_list)
        print()

    elif x == "2":
        print()
        my_library.show_library(total_list)
        print()
        print()
    elif x == "3":
        print()
        my_library.filter_library(total_list)
        print()

    elif x == "4":
        n = input("Eres empleado? (si/no): ")
        if n == "si":
            f = True
            while f == True:
                person = Employee(0)
                check = person.checkout()
                rent = Rental()
                personal_rent, total_list = rent.rent_book(check, day, total_list)
                if personal_rent != 0:
                    all_rent.append(personal_rent)
                    f = False
                else:
                    f = True

        elif n == "no":
            f = True
            while f == True:
                person = Customer(0)
                check = person.checkout()
                rent = Rental()
                personal_rent, total_list = rent.rent_book(check, day, total_list)
                if personal_rent != 0:
                    all_rent.append(personal_rent)
                    f = False
                else:
                    f = True

    elif x == "5":
        n = input("Eres empleado? (si/no): ")
        if n == "si":
            person = Employee(1)
            check = person.checkout()
            rent = Rental()
            print("Estos son los libros que has arrendado")
            max = person.show_rented_name(all_rent, check[0])
            print()
            total_list, all_debts = rent.return_book(all_rent, check[0], n, total_list, max, day, all_debts)

        elif n == "no":
            person = Customer(1)
            check = person.checkout()
            rent = Rental()
            print("Estos son los libros que has arrendado")
            max = person.show_rented_name(all_rent, check[0])
            print()
            total_list, all_debts = rent.return_book(all_rent, check[0], n, total_list, max, day, all_debts)

    elif x == "6":
        order = ["Nombre", "Numero serial", "Dia de arriendo", "Fecha de entrega", "Precio diario", "Precio de atraso", "Empleado"]
        print()
        print("{: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >10}".format(*order))
        for row in all_rent:
            print("{: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >17} | {: >10}".format(*row))
        print()

    elif x == "7":
        if len(all_debts) == 0:
            print("No hay deudas.")
        else:
            name = input("Cual es tu nombre?: ")
            for i in range(len(all_debts)):
                if name in all_debts[i]:
                    print(f"{name} debes {all_debts[i][0]}$")
                    pay = input("Quieres pagar la deuda? (si/no): ")
                    if pay == "si":
                        all_debts.pop(i)
                    else:
                        continue
    
    elif x == "8":
        pass

    else:
        break

    day += 1
    print("---------------")
    print(f"     Dia {day}     ")
    print("---------------")