import pickle
def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("show all- Show all books")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("save -  Save Catalog")
    print("load -  Load Catalog")
    print("clear -  Clear Catalog")
    print("exit - Exit program")


def show_all_book(book_catalog):
    for book in book_catalog:
        print(f"{book}: {book_catalog[book]['author']} {book_catalog[book]['pubyear']}")


def show_book(book_catalog):
    user_book = input("Enter name of the book: ")
    for book in book_catalog:
        if book.lower() == user_book.lower():
            print(f"Author: {book_catalog[user_book]['author']} \nYear:{book_catalog[user_book]['pubyear']}")
            break
    else:
        print(f"{user_book} not in the book catalog")


def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    if mode == "edit" and title not in book_catalog:
        print(f"{title} not in catalog")
        raise ValueError('Title not in catalog')
    if mode == "add" and title in book_catalog:
        print(f"{title} already in catalog")
        raise ValueError('Title already in catalog')
    year = int(input("Year: "))
    author = input("Author: ")
    book_catalog[title] = {'author': author, 'pubyear': year}


def delete_book(book_catalog):
    book = input("Enter book to delete: ")
    if book in book_catalog:
        del book_catalog[book]
        print(f"{book} has been removed.")
    else:
        print(f"{book} is not in the catalog.")


def save_catalog(book_catalog):
    with open("Book_catalog.bin", "wb") as file:
        pickle.dump(book_catalog, file)


def load_catalog(book_catalog):
    with open("Book_catalog.bin", "rb") as file:
        print(pickle.load(file))


def clear_catalog(book_catalog):
    book_catalog.clear()


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
        if command == "show all":
            show_all_book(book_catalog)
        elif command == "show":
            show_book(book_catalog)
        elif command == "add":
            try:
                add_edit_book(book_catalog, mode="add")
            except ValueError as err:
                print(err)
        elif command == "edit":
            try:
                add_edit_book(book_catalog, mode="edit")
            except ValueError as err:
                print(err)
        elif command == "del":
            delete_book(book_catalog)
        elif command == "save":
            save_catalog(book_catalog)
        elif command == "load":
            load_catalog(load_catalog)
        elif command == "clear":
            clear_catalog(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
