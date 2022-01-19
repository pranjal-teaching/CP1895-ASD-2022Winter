def show_book(book_catalog):
    user_book = input("Enter name of the book: ")
    for book in book_catalog:
        if book.lower() == user_book.lower():
            print(f"Author: {book_catalog[book]['author']}\nPublication year: {book_catalog[book]['pubyear']}")
            break
    else:
        print(f"{book} not in book catalog.")


def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    if mode == "edit" and title not in book_catalog:
        print("Title not in catalog.")
        raise ValueError('Title not in catalog.')
    elif mode == "add" and title in book_catalog:
        print("Title already in catalog.")
        raise ValueError('Title already in catalog.')
    pub_yr = input("Pub Year: ")
    author = input("Author: ")
    book_catalog[title] = {'author': author, 'pubyear': pub_yr}


def delete_book(book_catalog):
    title = input("Title to delete: ")
    if title in book_catalog:
        del book_catalog[title]
        print(title + " has been removed from catalog.")
    else:
        print(title + " is not in the catalog.")


def show_all_books(book_catalog):
    for book in book_catalog:
        print(f"{book}: {book_catalog[book]['author']} {book_catalog[book]['pubyear']}")


def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("load - Loads a saved catalog")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("show_all - Show all books")
    print("clear - Clear catalog")
    print("save - Save catalog")
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
        elif command == "show_all":
            show_all_books(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        elif command == "save":
            pass
        elif command == "load":
            pass
        elif command == "clear":
            pass
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
