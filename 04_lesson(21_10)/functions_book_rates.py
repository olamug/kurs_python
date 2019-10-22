# napisz funkcję, która pyta użytkownika
# o pary książka + ocena i zapisuje jej w programie.
#napisz fukcję, która zapyta o ocene książki i wyświetli film wraz z oceną
# jeśli film istnieje
# w prosty sposób obsłuż błąd uzytkwonika - użytkownik zapyta o nuemr w bazie, który nie istnieje

def add_book():
    dict_books = {}
    counter = int(input("Ile chcesz dodoać książek: "))
    for _ in range(counter):
        title = input("podaj tytuł: ")
        grade = input("podaj ocenę: ")
        dict_books[title] = grade # to się wcześniej nazywało books[title]

    return dict_books

books = add_book()
print(books)
# dodawanie jęsli ksiązka istenie
def read_book_by_grade(libr):
    g = input("podaj ocenę książki jaka chcesz przeczutać: ")
    if g in books.values():
        for title, grade in books.items():
            if grade == g:
                print(title, " - ocena:", grade)
    else:
        print("nie ma książki o takiej ocenie")
books = add_book()
print(books)
read_book_by_grade(books)