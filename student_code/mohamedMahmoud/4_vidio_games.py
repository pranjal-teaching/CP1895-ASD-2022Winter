import pickle


def save(book_catalog):
    with open("book_file.bin", "wb") as file:
        pickle.dump(book_catalog, file)


def load():
    with open("book_file.bin", "rb") as file:
        print(pickle.load(file))


def clear(book_catalog):
    book_catalog.clear()


def show_book(book_catalog):
    title = input('title: ')
    if title in book_catalog:
        book = book_catalog[title]
        print(f"title :     {title}")
        print(f"Author:     {book['author']}")
        print(f"pub year:   {book['pubyear']}")
    else:
        print(f"Sorry, {title} doesnt exist in the catalog.")


def add_book(book_catalog):
    title = input('title: ')
    if title in book_catalog:
        print(f"{title} is already in the book catalog ")

    else:
        book_author = input("Author: ")
        book_pubyear = input('pub year: ')
        book_catalog[title] = {"Author": book_author, "pubyear": book_pubyear}
        print(f"{title} has been added")


def edit_book(book_catalog):
    title = input('title: ')
    if title in book_catalog:
        book_author = input("Enter book author name update: ")
        book_pubyear = input('Enter book pub year update : ')
        book_catalog[title] = {"Author": book_author, "pubyear": book_pubyear}
        book = book_catalog[title]
        print('the book info has been updated')
        print(f"book title: {title}")
        print(f"Author: {book['Author']}")
        print(f"pubyear: {book['pubyear']}")
    else:
        print('the book not in catalog')


def delete_book(book_catalog):
    book = input("Enter name of the book: ")
    if book in book_catalog:
        del book_catalog[book]
        print(f"{book} has been deleted from the catalog.")
    else:
        print(f"{book} not in book catalog.")


def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("save -  Save Catalog")
    print("load -  Load Catalog")
    print("clear -  Clear Catalog")
    print("exit - Exit program")


def main():
    book_catalog = {
        "Moby Dick":
            {"author": "Herman Melville",
             "pubyear": "1851"},
        "The Hobbit":
            {"author": "J. R. R. Tolkien",
             "pubyear": "1937"},
        "Slaughterhouse Five":
            {"author": "Kurt Vonnegut",
             "pubyear": "1969"}
    }
    display_menu()
    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            show_book(book_catalog)
        elif command == "add":
            add_book(book_catalog)
        elif command == "edit":
            edit_book(book_catalog)
        elif command == "del":
            delete_book(book_catalog)
        elif command == "save":
            save(book_catalog)
        elif command == "load":
            load()
        elif command == "clear":
            clear(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
