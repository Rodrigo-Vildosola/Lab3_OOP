class Library:
    def __init__(self):
        self.categories = ["Nombre", "Autor", "Genero", "Precio", "Disponibilidad", "Numero de serie"]

    def show_library(self, list):
        print(list)
        self.list = list
        print("| {: >20} | {: >15} | {: >15} | {: >10} | {: >15} | {: >15} ".format(*self.categories))
        for row in self.list:
            print("| {: >20} | {: >15} | {: >15} | {: >10} | {: >13}   | {: >10} ".format(*row))

    def filter_library(self, list):
        self.list = list
        print("De que manera quieres filtrar?")
        n = input("(autor / genero): ")
        if n == "autor":
            author = input("Por cual autor quieres buscar?: ")
            print()
            print("| {: >20} | {: >15} | {: >15} | {: >10} | {: >15} | {: >15} ".format(*self.categories))
            for row in self.list:
                if author == row[1]:
                    print("| {: >20} | {: >15} | {: >15} | {: >10} | {: >13}   | {: >10} ".format(*row))

        elif n == "genero":
            genre = input("Por cual genero quieres buscar?: ")
            print()
            print()
            print("| {: >20} | {: >15} | {: >15} | {: >10} | {: >15} | {: >15} ".format(*self.categories))
            for row in self.list:
                if genre == row[2]:
                    print("| {: >20} | {: >15} | {: >15} | {: >10} | {: >13}   | {: >10} ".format(*row))

        

