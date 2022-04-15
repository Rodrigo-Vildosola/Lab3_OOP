

class Book:

    def __init__(self):
        t = True
        while t == True:
            self.name = input("Cual es el nombre del libro: ")
            self.author = input("Cual es el autor del libro: ")
            self.genre = input("Cual es el genero del libro: ")
            self.price = int(input("¿Cual es el precio del libro por dia?: "))
            self.quantity = int(input("¿Cuantos libros quieres agregar?: "))
            t = False


    def book_information(self):
        return [self.name, self.author, self.genre, self.price, self.quantity]
    