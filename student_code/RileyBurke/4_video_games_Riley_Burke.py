def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
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
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")


def add_edit_book(book_catalog, mode):
    if mode == "add":
        new_book_name = input("Enter book name: ")
        if new_book_name in book_catalog:
            print(f"{new_book_name} is already in the book catalog.")
        else:
            new_book_author = input("Enter book author: ")
            new_book_pubyear = input("Enter book publication year: ")
            book_catalog[new_book_name] = {"author": new_book_author, "pubyear": new_book_pubyear}
    elif mode == "edit":
        book_to_edit = input("Enter book to edit: ")
        if book_to_edit not in book_catalog:
            print(f"{book_to_edit} is not in the book catalog.")
        else:
            edit_author = input("Enter book author: ")
            edit_pubyear = input("Enter book publication year: ")
            book_catalog[book_to_edit] = {"author": edit_author, "pubyear": edit_pubyear}


def show_book(book_catalog):
    book = input("Enter name of the book: ")
    if book in book_catalog:
        print(f"Author: {book_catalog[book]['author']}\nPublication year: {book_catalog[book]['pubyear']}")
    else:
        print(f"{book} not in book catalog.")


def delete_book(book_catalog):
    book = input("Enter name of the book: ")
    if book in book_catalog:
        del book_catalog[book]
        print(f"{book} has been deleted from the catalog.")
    else:
        print(f"{book} not in book catalog.")


if __name__ == "__main__":
    main()
