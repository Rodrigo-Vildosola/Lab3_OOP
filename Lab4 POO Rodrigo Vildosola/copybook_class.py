from matplotlib.style import library


class Copybook:

    def __init__(self):

        self.serial_number = int(input("Cual es el numero de serie del libro: "))


    def final_info(self, book_info, library):
        if len(library[0]) != 0:
            if any(self.serial_number in sublist for sublist in library):
                for i in range(len(library)):
                    if library[i][5] == self.serial_number:
                        library[i][4] += book_info[4]
                        return library

            elif not (any(self.serial_number in sublist for sublist in library)):
                book_info.append(self.serial_number)
                library.append(book_info)
                return library
    
        elif len(library[0]) == 0:
            library.pop(0)
            book_info.append(self.serial_number)
            library.append(book_info)
            return library


